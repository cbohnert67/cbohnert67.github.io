# Portfolio de Cédric Bohnert & Méthode Liouaï

Bienvenue sur le dépôt de mon site personnel et espace d'apprentissage dialectique. Ce projet combine mon portfolio professionnel de développeur et l'espace **Méthode Liouaï**, une plateforme éducative interactive dédiée à l'apprentissage actif des mathématiques et du code.

---

## 🌟 Présentation Générale

Ce site est conçu comme une **Single Page Application (SPA)** fluide et performante. Il héberge deux espaces distincts et synchronisés :
1. **Le Portfolio Personnel** : Présentation de mon profil de *life-long learner autodidacte*, de mes compétences clés (Python, Modélisation, JavaScript, Agilité) et de mes réalisations majeures (MathsQuest, La Data Science de A à Z).
2. **La Méthode Liouaï** : Un espace de blog dialectique où je déconstruis des concepts complexes de mathématiques supérieures en utilisant l'IA comme un tuteur socratique.

---

## 🛠️ Stack Technique

L'application est construite avec des technologies légères, modernes et hautement performantes :
* **Core** : HTML5 sémantique et JavaScript Vanilla (ES6) pour le routage dynamique et les transitions d'affichage.
* **Design & Responsive** : [Tailwind CSS](https://tailwindcss.com/) pour un design fluide, épuré, premium, et une gestion automatique des modes clair/sombre.
* **Formules Mathématiques** : [MathJax](https://www.mathjax.org/) pour le rendu vectoriel de haute précision des expressions en $\LaTeX$.
* **Coloration Syntaxique** : [Highlight.js](https://highlightjs.org/) pour la mise en valeur élégante des blocs de code source (Python, JavaScript, etc.).
* **Effets Visuels** : [Particles.js](https://vincentgarreau.com/particles.js/) pour l'arrière-plan de la section Héros, créant un effet réseau dynamique et immersif.

---

## 🧠 La Philosophie "Méthode Liouaï"

La **Méthode Liouaï** (*Learn It Yourself*) est un manifeste pour un apprentissage autonome, critique et profond :
* **Dialogue Socratique** : L'IA n'est pas utilisée pour donner des réponses prémâchées, mais comme un tuteur qui pose des questions ciblées pour faire accoucher l'apprenant de sa propre intuition logique.
* **Raisonnement Rétroactif** : Passer de la lecture passive à l'explicabilité active en décortiquant les démonstrations théoriques (comme la densité de $\mathbb{Q}$ dans $\mathbb{R}$).

---

## 📂 Structure du Projet

```text
├── index.html          # Fiche unique de l'application de production (Portfolio & Méthode)
├── .agents/            # Configuration et scripts automatisés pour l'intégration de contenu
│   ├── AGENTS.md       # Consignes de l'équipe de développement de contenu
│   └── skills/         # Outils d'intégration automatique pour les agents de codage
├── articles/           # Dossier contenant les articles sources au format Markdown et HTML
│   ├── analyse/        # Articles classés par matière (ex: entre-deux-nombres.md)
│   └── ...
├── images/             # Actifs graphiques du site (photo de profil, favicon, etc.)
└── README.md           # Ce guide d'explication
```

---

## ✍️ Comment ajouter un nouvel article (Automatisation)

Le projet intègre un module automatisé (`.agents/skills/add_article/`) permettant à un script Python ou à un agent d'intégrer à la volée un nouvel article rédigé au format Markdown standard dans le fichier de production `index.html`.

### Processus automatisé :
1. **Parse & Extraction** : Analyse du frontmatter du fichier Markdown (Titre, Date, Résumé d'accroche, Catégories).
2. **Sécurisation LaTeX** : Remplacement automatique des opérateurs complexes (ex: `<` ou `>` dans les balises mathématiques) par leurs équivalents robustes $\LaTeX$ (`\lt` et `\gt`) pour éviter les conflits de rendu HTML.
3. **Mise en Page Prose** : Conversion sémantique des styles (paragraphes justifiés, citations stylisées, blocs de code pour Highlight.js).
4. **Insertion Directe** : Injection dynamique de la nouvelle section de lecture `<section id="view-[slug]">` et de la carte d'aperçu interactive au sommet du catalogue d'articles.

---

## 🚀 Déploiement

Le site est hébergé via **GitHub Pages**. Toute modification poussée sur la branche `main` déclenche le déploiement automatique du site à l'adresse :
🔗 **[cbohnert67.github.io](https://cbohnert67.github.io/index.html)**
