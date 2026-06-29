---
name: add_article
description: Intégrer un nouvel article Markdown dans le Portail SPA
---

# Skill: Intégrer un nouvel article Markdown dans le Portail SPA

Ce skill permet de prendre un fichier Markdown de votre choix dans le workspace et de l'injecter de bout en bout dans l'application `index.html`.

## Paramètres d'entrée
- `<markdown_path>` : Chemin vers le fichier Markdown de l'article (ex: `articles/les-fractions-continues.md`).
- `<categories>` : Liste de catégories séparées par des espaces (ex: `analyse bientot` ou `methodologie`).

## Processus d'Exécution pas à pas

### Étape 1 : Analyse et extraction (Content_Editor)
1. Charger le fichier situé à `<markdown_path>`.
2. Extraire les métadonnées de l'article (soit depuis le frontmatter YAML au début, soit à partir des premiers paragraphes/titres) :
   - `[TITLE]` : Le titre principal (généralement le `# Titre`).
   - `[SLUG]` : Une version normalisée, en minuscules et sans accent du titre (ex: `les-fractions-continues`).
   - `[EXCERPT]` : Une phrase d'introduction accrocheuse ou les 3 premières lignes de l'article pour servir de résumé sur la carte.
   - `[TAGS]` : Titres stylisés des catégories (ex: `Algèbre • Méthode`).
   - `[DATE]` : La date courante ou spécifiée.

### Étape 2 : Nettoyage et sécurisation du LaTeX (Content_Editor)
- Scanner toutes les équations comprises entre `$` ou `$$`.
- Remplacer chaque occurrence de `<` par `\lt` et `>` par `\gt` uniquement au sein des délimiteurs mathématiques.
- Convertir le corps du markdown en balises HTML élégantes :
  - Paragraphes normaux -> `<p class="justified-p">...</p>`
  - Citations importantes -> Encadrées par `<div class="my-8 p-6 bg-stone-100 dark:bg-stone-900 rounded-xl border border-stone-200 dark:border-stone-800 shadow-sm">`
  - Blocs de codes -> Garder la structure `<pre><code class="language-[lang]">...</code></pre>` requise par Highlight.js.

### Étape 3 : Injection dans le code source de l'application (Frontend_Integrator)
1. **Ajouter la vue d'article dans le corps HTML** :
   - Ouvrir `index.html`.
   - Repérer la balise de fin de la zone principale : `</main>`.
   - Injecter juste avant celle-ci la nouvelle section de l'article en suivant précisément ce canevas structurel :
   ```html
   <!-- ARTICLE VIEW: [SLUG_EN_MAJUSCULES] -->
   <section id="view-[SLUG]" class="view-section hidden max-w-3xl mx-auto px-6 py-12 md:py-20">
       <div class="mb-10">
           <button onclick="navigateTo('home')" class="group inline-flex items-center text-sm font-semibold text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-white transition-colors">
               <svg class="w-4 h-4 mr-2 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
               Retour à l'accueil
           </button>
       </div>

       <article class="prose prose-stone dark:prose-invert max-w-none">
           <header class="mb-12">
               <div class="flex items-center space-x-2 text-stone-500 dark:text-stone-400 text-sm font-medium mb-3">
                   <span>[TAGS_EN_MAJUSCULES]</span>
                   <span>•</span>
                   <span>MATHÉMATIQUES & IA</span>
               </div>
               <h1 class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-stone-900 dark:text-white leading-tight mb-6 tracking-tight">
                   [TITLE]
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
           <div class="space-y-6 text-lg text-stone-700 dark:text-stone-300">
               [ARTICLE_HTML_CONTENT]
           </div>
       </article>

       <div class="mt-16 pt-8 border-t border-stone-200 dark:border-stone-800">
           <button onclick="navigateTo('home')" class="group inline-flex items-center text-sm font-semibold text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-white transition-colors">
               <svg class="w-4 h-4 mr-2 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
               Retour au catalogue d'articles
           </button>
       </div>
   </section>
   ```

2. **Créer et positionner la carte d'aperçu dans le catalogue d'accueil** :
   - Trouver l'élément `<div id="catalog-grid" class="grid gap-8 md:grid-cols-2">` dans la section `view-home`.
   - Insérer la nouvelle carte interactive tout en haut du conteneur (les articles les plus récents en premier) :
   ```html
   <!-- Card: [TITLE] (Active) -->
   <div class="group cursor-pointer bg-white dark:bg-stone-900/40 border border-stone-200 dark:border-stone-800/80 rounded-2xl p-6 shadow-sm hover:shadow-md hover:border-stone-400 dark:hover:border-stone-700 transition-all flex flex-col justify-between" 
        data-category="[categories]" 
        onclick="navigateTo('article-[SLUG]')">
       <div>
           <div class="flex items-center justify-between mb-4">
               <span class="text-[10px] font-mono tracking-widest uppercase font-bold text-sky-600 dark:text-sky-400">[TAGS]</span>
               <span class="text-xs text-stone-500">[DATE]</span>
           </div>
           <h3 class="text-xl font-bold text-stone-900 dark:text-white group-hover:text-stone-700 dark:group-hover:text-stone-300 transition-colors mb-3">
               [TITLE]
           </h3>
           <p class="text-sm text-stone-600 dark:text-stone-400 line-clamp-3 mb-6 justified-p">
               [EXCERPT]
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
   ```

### Étape 4 : Validation finale
- Vérifier la structure HTML générée (balises fermantes).
- Exécuter un aperçu de l'application pour tester que la navigation vers l'article s'effectue correctement et que le rafraîchissement MathJax s'active.
