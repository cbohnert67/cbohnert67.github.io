import re
import sys
import yaml # pyyaml is usually installed, but to be safe we can use a basic regex/string split frontmatter parser

def parse_frontmatter(content):
    # Regex to extract frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    
    fm_text = match.group(1)
    body = match.group(2)
    
    metadata = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            metadata[key.strip()] = val.strip().strip('"').strip("'")
            
    return metadata, body

def secure_latex(text):
    # Replace < and > inside $...$ and $$...$$
    
    # 1. First process display math $$...$$
    def replace_display(match):
        formula = match.group(1)
        formula = formula.replace('<', r'\lt').replace('>', r'\gt')
        return '$$' + formula + '$$'
    
    text = re.sub(r'\$\$(.*?)\$\$', replace_display, text, flags=re.DOTALL)
    
    # 2. Process inline math $...$
    def replace_inline(match):
        formula = match.group(1)
        formula = formula.replace('<', r'\lt').replace('>', r'\gt')
        return '$' + formula + '$'
    
    # Avoid matching math inside html attributes or scripts (though usually fine in md)
    text = re.sub(r'\$([^\$\n]+?)\$', replace_inline, text)
    
    return text

def parse_inline_elements(text):
    # Convert bold **text** to <strong class="text-stone-950 dark:text-white">text</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-stone-950 dark:text-white">\1</strong>', text)
    
    # Convert italic *text* to <em>text</em>
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    return text

def convert_markdown_to_html(body):
    lines = body.split('\n')
    html_blocks = []
    
    in_code_block = False
    code_lang = ""
    code_content = []
    
    in_blockquote = False
    blockquote_lines = []
    
    in_dialogue = False
    dialogue_items = []
    
    # To group paragraphs nicely
    in_paragraph_group = False
    paragraph_group_class = "space-y-6 text-lg text-stone-700 dark:text-stone-300"
    current_paragraph_group = []
    
    def flush_paragraph_group():
        nonlocal in_paragraph_group, current_paragraph_group
        if in_paragraph_group and current_paragraph_group:
            html_blocks.append(f'<div class="{paragraph_group_class}">\n' + "\n".join(current_paragraph_group) + '\n</div>')
            current_paragraph_group = []
            in_paragraph_group = False

    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check code blocks
        if line.strip().startswith('```'):
            flush_paragraph_group()
            if not in_code_block:
                in_code_block = True
                code_lang = line.strip()[3:].strip()
                code_content = []
            else:
                in_code_block = False
                # Format code block according to Liouaï style
                lang_display = "Python 3" if code_lang.lower() == 'python' else code_lang.upper()
                filename = "simulation.py" if code_lang.lower() == 'python' else "script"
                
                code_html = f"""<div class="my-8 rounded-xl overflow-hidden border border-stone-200 dark:border-stone-800 shadow-lg">
    <div class="bg-stone-800 text-stone-400 px-6 py-3 flex justify-between items-center">
        <span class="text-xs font-mono font-bold">{filename}</span>
        <span class="text-[10px] bg-stone-700 px-2.5 py-1 rounded text-stone-300 uppercase tracking-widest font-mono">{lang_display}</span>
    </div>
    <pre class="m-0 p-0 rounded-none"><code class="language-{code_lang}">{"".join(code_content)}</code></pre>
</div>"""
                html_blocks.append(code_html)
            i += 1
            continue
            
        if in_code_block:
            code_content.append(line + '\n')
            i += 1
            continue
            
        # Check blockquotes
        if line.strip().startswith('>'):
            flush_paragraph_group()
            in_blockquote = True
            blockquote_lines.append(line.strip()[1:].strip())
            i += 1
            continue
        elif in_blockquote:
            # End of blockquote
            in_blockquote = False
            
            # Format blockquote
            bq_content = "\n".join(blockquote_lines)
            
            if "journal intérieur" in bq_content:
                # Journal interior style
                clean_content = bq_content.replace('**Extrait de mon journal intérieur**', '').replace('Extrait de mon journal intérieur', '').strip()
                clean_content = clean_content.strip('«').strip('»').strip()
                clean_content = parse_inline_elements(clean_content)
                html_blocks.append(f"""<div class="my-8 p-6 bg-stone-100 dark:bg-stone-900 rounded-xl border border-stone-200 dark:border-stone-800 shadow-sm">
    <div class="text-xs font-mono text-stone-500 dark:text-stone-400 uppercase tracking-widest mb-2">Extrait de mon journal intérieur</div>
    <p class="italic text-stone-800 dark:text-stone-200 font-serif leading-relaxed text-lg">
        « {clean_content} »
    </p>
</div>""")
            elif "puristes" in bq_content.lower():
                # Note for purists style
                clean_content = bq_content.replace('**Note pour les puristes :**', '').replace('Note pour les puristes :', '').strip()
                clean_content = parse_inline_elements(clean_content)
                html_blocks.append(f"""<div class="my-8 p-6 bg-amber-50 dark:bg-amber-950/20 rounded-xl border border-amber-200 dark:border-amber-900/40 text-stone-800 dark:text-stone-300">
    <p class="justified-p font-semibold text-amber-900 dark:text-amber-400 mb-2">Note pour les puristes :</p>
    <p class="justified-p text-sm">
        {clean_content}
    </p>
</div>""")
            else:
                # Default citation style
                clean_content = parse_inline_elements(bq_content)
                html_blocks.append(f"""<div class="my-8 p-6 bg-stone-100 dark:bg-stone-900 rounded-xl border border-stone-200 dark:border-stone-800 shadow-sm">
    <p class="italic text-stone-800 dark:text-stone-200 font-serif leading-relaxed text-lg">
        {clean_content}
    </p>
</div>""")
            blockquote_lines = []
            
        # Check dialogue
        # A list item starting with "- **Moi** :" or "- **Gemini** :"
        is_dialogue_line = False
        if line.strip().startswith('-'):
            stripped = line.strip()[1:].strip()
            if stripped.startswith('**Moi**') or stripped.startswith('**Gemini**'):
                is_dialogue_line = True
                
        if is_dialogue_line:
            flush_paragraph_group()
            in_dialogue = True
            # Parse line
            stripped = line.strip()[1:].strip()
            speaker = "Moi" if stripped.startswith('**Moi**') else "Gemini"
            content = stripped.split(':', 1)[1].strip()
            # strip formatting
            content = content.strip('*').strip('_').strip('"').strip("'").strip('«').strip('»').strip()
            content = parse_inline_elements(content)
            
            speaker_class = "bg-teal-100 dark:bg-teal-950/50 text-teal-800 dark:text-teal-300" if speaker == "Moi" else "bg-amber-100 dark:bg-amber-950/50 text-amber-800 dark:text-amber-300"
            
            dialogue_items.append(f"""<div class="pt-4">
    <span class="inline-block text-xs font-bold font-mono px-2 py-1 {speaker_class} rounded mb-2">{speaker}</span>
    <p class="{"italic " if speaker == "Moi" else ""}text-stone-800 dark:text-stone-200">"{content}"</p>
</div>""")
            i += 1
            continue
        elif in_dialogue and not is_dialogue_line:
            # End of dialogue block
            in_dialogue = False
            dialogue_html = f"""<div class="my-8 rounded-xl border border-stone-200 dark:border-stone-800 shadow-md overflow-hidden">
    <div class="bg-stone-200 dark:bg-stone-900 px-6 py-3 border-b border-stone-200 dark:border-stone-800 flex justify-between items-center">
        <span class="text-xs font-mono uppercase tracking-widest text-stone-600 dark:text-stone-400 font-bold">Transcription Socratique : Gemini &amp; Moi</span>
        <span class="w-3.5 h-3.5 rounded-full bg-emerald-500"></span>
    </div>
    <div class="p-6 bg-white dark:bg-stone-900/40 divide-y divide-stone-100 dark:divide-stone-800/60 space-y-4">
        {"".join(dialogue_items)}
    </div>
</div>"""
            html_blocks.append(dialogue_html)
            dialogue_items = []
            
        # Check headings
        if line.strip().startswith('###'):
            flush_paragraph_group()
            heading_text = line.strip()[3:].strip()
            html_blocks.append(f'<h3 class="text-xl font-bold text-stone-900 dark:text-white mb-3">{heading_text}</h3>')
            i += 1
            continue
        elif line.strip().startswith('##'):
            flush_paragraph_group()
            heading_text = line.strip()[2:].strip()
            html_blocks.append(f'<h2 class="text-2xl md:text-3xl font-bold text-stone-900 dark:text-white mt-12 mb-6 border-b border-stone-200 dark:border-stone-800 pb-2">{heading_text}</h2>')
            i += 1
            continue
        elif line.strip().startswith('#'):
            flush_paragraph_group()
            # Title is parsed, we don't output # h1 in the article body because it's handled in the article header
            i += 1
            continue
            
        # Normal paragraphs
        if line.strip():
            # If not inside a paragraph group, start one
            if not in_paragraph_group:
                in_paragraph_group = True
                paragraph_group_class = "space-y-6 text-lg text-stone-700 dark:text-stone-300"
                # Check if it is a conclusion or regular paragraph
                # But actually keeping it standard is perfect
                
            parsed_line = parse_inline_elements(line.strip())
            
            # Check if this paragraph has specific styling like bold class for Liouaï definition
            if parsed_line.startswith('La méthode <strong') or parsed_line.startswith('La Méthode <strong'):
                current_paragraph_group.append(f'<p class="justified-p font-semibold border-l-4 border-stone-800 dark:border-stone-300 pl-4 py-1 text-stone-900 dark:text-stone-100">\n    {parsed_line}\n</p>')
            elif "Et vous, quel est" in parsed_line:
                current_paragraph_group.append(f'<p class="justified-p font-bold text-stone-900 dark:text-stone-100 text-xl pt-4">\n    {parsed_line}\n</p>')
            else:
                current_paragraph_group.append(f'<p class="justified-p">\n    {parsed_line}\n</p>')
        else:
            # Empty line can signify end of a paragraph group if we want, or just spacing. Let's keep it.
            pass
            
        i += 1
        
    # Flush any remaining block groups
    flush_paragraph_group()
    if in_blockquote:
        # handle end
        pass
    if in_dialogue:
        # handle end
        pass
        
    return "\n\n".join(html_blocks)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python parse_markdown.py <markdown_path>")
        sys.exit(1)
        
    md_path = sys.argv[1]
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    metadata, body = parse_frontmatter(content)
    body_secured = secure_latex(body)
    html_content = convert_markdown_to_html(body_secured)
    
    # Print out JSON string containing all parameters
    import json
    result = {
        "title": metadata.get("title", "Sans Titre"),
        "slug": metadata.get("slug", "sans-titre"),
        "excerpt": metadata.get("excerpt", ""),
        "tags": metadata.get("tags", ""),
        "date": metadata.get("date", ""),
        "categories": metadata.get("categories", ""),
        "html": html_content
    }
    print(json.dumps(result, ensure_ascii=False))
