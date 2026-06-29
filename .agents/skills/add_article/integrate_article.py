import sys
import re
import os
import json
from parse_markdown import parse_frontmatter, secure_latex, convert_markdown_to_html

def main():
    if len(sys.argv) < 3:
        print("Usage: python integrate_article.py <markdown_path> <index_html_path>")
        sys.exit(1)
        
    md_path = sys.argv[1]
    html_path = sys.argv[2]
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
        
    metadata, body = parse_frontmatter(md_content)
    body_secured = secure_latex(body)
    html_content = convert_markdown_to_html(body_secured)
    
    title = metadata.get("title", "Sans Titre")
    slug = metadata.get("slug", "sans-titre")
    excerpt = metadata.get("excerpt", "")
    tags = metadata.get("tags", "")
    date = metadata.get("date", "")
    categories = metadata.get("categories", "")
    
    # Read index.html
    with open(html_path, 'r', encoding='utf-8') as f:
        html_file_content = f.read()
        
    slug_upper = slug.upper()
    tags_upper = tags.upper()
    
    # Construct the section view html
    section_html = f"""
        <!-- ARTICLE VIEW: {slug_upper} -->
        <section id="view-article-{slug}" class="view-section hidden max-w-5xl mx-auto px-6 py-12 md:py-20">
            <div class="mb-10">
                <button onclick="navigateTo('home')" class="group inline-flex items-center text-sm font-semibold text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-white transition-colors">
                    <svg class="w-4 h-4 mr-2 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                    Retour à l'accueil
                </button>
            </div>

            <article class="prose prose-stone dark:prose-invert max-w-none">
                <header class="mb-12">
                    <div class="flex items-center space-x-2 text-stone-500 dark:text-stone-400 text-sm font-medium mb-3">
                        <span>{tags_upper}</span>
                        <span>•</span>
                        <span>MATHÉMATIQUES & IA</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-stone-900 dark:text-white leading-tight mb-6 tracking-tight">
                        {title}
                    </h1>
                    <div class="flex items-center space-x-3 text-stone-600 dark:text-stone-400 text-sm border-y border-stone-200 dark:border-stone-800 py-3">
                        <div class="w-8 h-8 rounded-full bg-stone-800 text-stone-100 flex items-center justify-center font-bold text-xs">C</div>
                        <div>
                            <span class="font-semibold text-stone-900 dark:text-stone-200">Par Cédric</span>
                            <span class="mx-1">•</span>
                            <span>Créateur de la méthode Liouaï</span>
                        </div>
                    </div>
                </header>
                {html_content}
            </article>

            <div class="mt-16 pt-8 border-t border-stone-200 dark:border-stone-800">
                <button onclick="navigateTo('home')" class="group inline-flex items-center text-sm font-semibold text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-white transition-colors">
                    <svg class="w-4 h-4 mr-2 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                    Retour au catalogue d'articles
                </button>
            </div>
        </section>
    """
    
    if f'view-article-{slug}' in html_file_content:
        print(f"Article view view-article-{slug} already exists. Replacing it.")
        pattern = rf'<!-- ARTICLE VIEW: {slug_upper} -->.*?/section>'
        html_file_content = re.sub(pattern, lambda m: section_html.strip(), html_file_content, flags=re.DOTALL)
    else:
        main_index = html_file_content.rfind('</main>')
        if main_index == -1:
            print("Error: </main> not found in index.html")
            sys.exit(1)
        html_file_content = html_file_content[:main_index] + section_html + "\n    " + html_file_content[main_index:]
        
    # Inject the card inside #catalog-grid
    card_html = f"""
                <!-- Card: {title} (Active) -->
                <div class="group cursor-pointer bg-white dark:bg-stone-900/40 border border-stone-200 dark:border-stone-800/80 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-stone-400 dark:hover:border-stone-700 transition-all flex flex-col justify-between" 
                     data-category="{categories}" 
                     onclick="navigateTo('article-{slug}')">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="text-[10px] font-mono tracking-widest uppercase font-bold text-teal-600 dark:text-teal-400">{tags}</span>
                            <span class="text-xs text-stone-500">{date}</span>
                        </div>
                        <h3 class="text-xl font-bold text-stone-900 dark:text-white group-hover:text-stone-700 dark:group-hover:text-stone-300 transition-colors mb-3">
                            {title}
                        </h3>
                        <p class="text-sm text-stone-600 dark:text-stone-400 line-clamp-3 mb-6 justified-p">
                            {excerpt}
                        </p>
                    </div>
                    <div class="flex items-center justify-between pt-4 border-t border-stone-100 dark:border-stone-800/60">
                        <div class="flex items-center space-x-2 text-xs">
                            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                            <span class="font-semibold text-stone-700 dark:text-stone-300">Article complet disponible</span>
                        </div>
                        <span class="text-xs font-bold text-stone-900 dark:text-stone-100 group-hover:translate-x-1 transition-transform inline-flex items-center">
                            Lire la suite 
                            <svg class="w-3.5 h-3.5 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                        </span>
                    </div>
                </div>
    """
    
    grid_pattern = r'(<div id="catalog-grid" class="[^"]*">)'
    match = re.search(grid_pattern, html_file_content)
    if not match:
        print("Error: #catalog-grid not found in index.html")
        sys.exit(1)
        
    grid_start_idx = match.end()
    
    card_comment = f'<!-- Card: {title} (Active) -->'
    if card_comment in html_file_content:
        print("Card already exists. Skipping duplicate insert.")
    else:
        html_file_content = html_file_content[:grid_start_idx] + card_html + html_file_content[grid_start_idx:]
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_file_content)
        
    print(f"Successfully integrated article '{title}' into '{html_path}'!")

if __name__ == '__main__':
    main()
