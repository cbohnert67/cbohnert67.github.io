import sys
from html.parser import HTMLParser

class LiouaiHTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags_stack = []
        
        # Target elements
        self.article_section_found = False
        self.density_card_found = False
        self.socratique_card_found = False
        self.cantor_card_found = False
        self.non_euclidean_card_found = False
        
        self.found_filters = set()
        self.in_catalog_grid = False
        self.catalog_grid_depth = 0
        self.current_card_category = None
        
    def handle_starttag(self, tag, attrs):
        self.tags_stack.append(tag)
        attrs_dict = dict(attrs)
        
        # Check filter buttons
        onclick_val = attrs_dict.get('onclick', '')
        if onclick_val.startswith('filterCategory('):
            # Extract category name
            cat = onclick_val.split("'", 2)[1]
            self.found_filters.add(cat)
            
        # Check catalog-grid
        if tag == 'div' and attrs_dict.get('id') == 'catalog-grid':
            self.in_catalog_grid = True
            self.catalog_grid_depth = len(self.tags_stack)
            
        # Check if we are inside catalog grid and see cards
        if self.in_catalog_grid and tag == 'div':
            onclick_val = attrs_dict.get('onclick', '')
            data_cat = attrs_dict.get('data-category', '')
            
            if 'article-entre-deux-nombres' in onclick_val:
                self.density_card_found = True
            elif data_cat == 'socratique':
                self.socratique_card_found = True
            elif data_cat == 'analyse':
                self.cantor_card_found = True
            elif data_cat == 'fondations':
                self.non_euclidean_card_found = True
                
        # Check section view-article-entre-deux-nombres
        if tag == 'section' and attrs_dict.get('id') == 'view-article-entre-deux-nombres':
            self.article_section_found = True
            
    def handle_endtag(self, tag):
        if not self.tags_stack:
            return
            
        last_tag = self.tags_stack.pop()
        
        if self.in_catalog_grid and len(self.tags_stack) < self.catalog_grid_depth:
            self.in_catalog_grid = False

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_html.py <html_path>")
        sys.exit(1)
        
    html_path = sys.argv[1]
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    validator = LiouaiHTMLValidator()
    validator.feed(content)
    
    errors = 0
    print("\n--- NEW TAXONOMY VALIDATION RESULTS ---")
    
    # 1. Section check
    if validator.article_section_found:
        print("[OK] Section 'view-article-entre-deux-nombres' is present.")
    else:
        print("[FAIL] Section 'view-article-entre-deux-nombres' was NOT found.")
        errors += 1
        
    # 2. Card check
    if validator.density_card_found:
        print("[OK] Card for 'article-entre-deux-nombres' is present.")
    else:
        print("[FAIL] Card for 'article-entre-deux-nombres' was NOT found.")
        errors += 1
        
    # 3. Placeholders check
    if not validator.socratique_card_found:
        print("[OK] Socratic Prompting card placeholder was removed.")
    else:
        print("[FAIL] Socratic Prompting card placeholder is still present!")
        errors += 1
        
    if not validator.cantor_card_found:
        print("[OK] Cantor's Diagonal card placeholder was removed.")
    else:
        print("[FAIL] Cantor's Diagonal card placeholder is still present!")
        errors += 1
        
    if not validator.non_euclidean_card_found:
        print("[OK] Non-Euclidean Geometry card placeholder was removed.")
    else:
        print("[FAIL] Non-Euclidean Geometry card placeholder is still present!")
        errors += 1
        
    # 4. Filters check
    expected_filters = {'all', 'methodologie', 'socratique', 'fondations', 'algebre', 'analyse', 'code'}
    missing_filters = expected_filters - validator.found_filters
    
    if not missing_filters:
        print("[OK] All 7 taxonomy filter buttons are present in HTML.")
    else:
        print(f"[FAIL] Missing taxonomy filter buttons: {missing_filters}")
        errors += 1
        
    # 5. JS list verification
    # Find filters array in content
    js_filters_match = re.search(r'const\s+filters\s*=\s*\[(.*?)\]', content)
    if js_filters_match:
        filters_str = js_filters_match.group(1)
        filters_list = [f.strip().strip("'").strip('"') for f in filters_str.split(',')]
        if set(filters_list) == expected_filters:
            print("[OK] JS filters array matches exactly the new taxonomy.")
        else:
            print(f"[FAIL] JS filters array mismatched. Found: {filters_list}")
            errors += 1
    else:
        print("[FAIL] JS filters list was not parsed from index.html.")
        errors += 1
        
    if errors == 0:
        print("\nAll taxonomy validation checks PASSED successfully!")
        sys.exit(0)
    else:
        print(f"\nTaxonomy validation FAILED with {errors} errors.")
        sys.exit(1)

if __name__ == '__main__':
    import re
    main()
