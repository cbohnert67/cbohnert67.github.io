---
title: "Entre deux nombres, il y a toujours un monde : comment j'ai apprivoisé la densité des rationnels grâce à l'IA."
slug: "entre-deux-nombres"
excerpt: "Quand on entre à l’université pour préparer une Licence de Mathématiques, le saut conceptuel entre les méthodes du lycée et celles de la L1 procure souvent un sentiment de vertige. Découvrez comment déconstruire et visualiser la densité de $\mathbb{Q}$ dans $\mathbb{R}$."
tags: "Analyse • Méthodologie"
date: "Mars 2026"
categories: "analyse methodologie"
---

# Entre deux nombres, il y a toujours un monde : comment j'ai apprivoisé la densité des rationnels grâce à l'IA.

Quand on entre à l’université pour préparer une Licence de Mathématiques, le saut conceptuel entre les méthodes du lycée et celles de la L1 procure souvent un sentiment de vertige. L’abstraction pure s'impose dès les premiers jours. Fini le temps des "recettes" de calcul : place à la déconstruction systématique des définitions et des théorèmes. Un changement de paradigme qui peut déstabiliser, même les meilleurs. Imaginez alors un adulte, solitaire et autodidacte, qui décide de plonger dans ce vaste univers sans guide.

J’ai toujours aimé apprendre en profondeur. Pourtant, en ouvrant mes premiers manuels du supérieur — les classiques Liret-Martinais ou Monier — je me suis vite heurté à un mur. Des heures passées à lire, à relire, pour finalement rester avec ce sentiment d’échec : je n'avais pas la bonne clé de lecture.

J'ai fini par trouver une solution : **aborder le cours avec l'IA**. En utilisant Gemini comme un partenaire socratique, j'ai transformé une expérience de lecture passive en un dialogue actif et fructueux.

Pour illustrer cette méthode, je vous propose de revenir sur ma première rencontre, particulièrement douloureuse, avec un concept qui m'a longtemps hanté : **la densité des rationnels dans les réels.**

On nous apprend, enfants, que les nombres sont comme des marches d'escalier : après 1, il y a 2. Une illusion rassurante de "voisins immédiats". Mais cette image vole en éclats dès que l'on manipule les réels : entre deux nombres, aussi proches soient-ils, se cache une infinité de rationnels. Comment visualiser un espace où, quel que soit le niveau de zoom, il n'y a jamais de "fond" ?

C’est ce vertige de l’infini qui m’a longtemps bloqué. J'ai compris que mon erreur était de vouloir *contenir* l'infini plutôt que de dialoguer avec lui. C’est là que la **Méthode Liouaï** est née : utiliser l’IA non comme une encyclopédie froide, mais comme un tuteur socratique pour déconstruire mes blocages.

Voici comment, en une séance de travail, cette approche m’a permis de passer de l’incompréhension totale à ce moment de clarté que l’on nomme le moment "Aha !".

## Le "Mur"

Mon premier vrai combat avec le Monier a porté sur la densité de $\mathbb{Q}$ dans $\mathbb{R}$. J'étais face à une contradiction qui me semblait insoluble : d'un côté, je lisais que les rationnels sont "dénombrables", alors que les réels sont "indénombrables". Si compter les rationnels est concevable, découvrir que les réels échappent à toute énumération est une autre paire de manches.

Intuitivement, mon cerveau classait les rationnels comme étant "plus petits" ou plus "rares" que les réels comme $\pi$ ou $\sqrt{2}$. Il s’avère pourtant que c’est le contraire : $\mathbb{R}$ est infiniment plus "gros" que $\mathbb{Q}$. Et pourtant, le théorème de densité affirme qu'entre deux réels, il existe toujours un rationnel. Comment quelque chose de "plus petit" peut-il être omniprésent au point de remplir chaque interstice ? Cette dissonance cognitive est devenue mon mur. Un mur qui m'empêchait d'avancer.

> **Extrait de mon journal intérieur**
> « Je ne comprends pas. La propriété dit : "Soit $x < y$, il existe un rationnel $r$ tel que $x < r < y$". C'est logique sur le papier, mais mon cerveau ne le "voit" pas. Si je prends $0,33$ et $0,34$, je vois bien $0,335$. Mais si je prends des irrationnels, je suis perdu. Je n'arrive pas à visualiser la densité. Je suis bloqué. »

J'ai fini par comprendre, quelques années plus tard, que le problème ne venait ni des mathématiques, ni de la rigueur du manuel, mais de la nature même de mon dialogue avec le savoir.

## Le Dialogue Socratique

Au début, j'ai utilisé l'IA comme un livre interactif. Mais ce mur se fissurait à peine. L'IA me déroulait des preuves standards, froides, "prêtes-à-penser". Un véritable perroquet savant dont le discours glissait sur mon esprit sans s'y accrocher. J'ai même tenté le *prompt engineering* classique, sans réelle satisfaction. Il manquait l'essentiel : la dialectique.

C'est en découvrant l'approche socratique que j'ai repris espoir. J'ai décidé d'inverser les rôles. J'ai configuré mon environnement pour que l'IA ne me donne plus jamais de solution directe. J'ai exigé un dialogue.

### Transcription Socratique : Gemini & Moi

- **Moi** : *"J'ai l'intuition que les rationnels sont plus 'petits' que les réels, mais on me dit qu'ils sont denses. Peux-tu me demander une série de questions pour tester ma compréhension, sans me donner la preuve tout de suite ?"*
- **Gemini** : *"C'est une excellente approche. Commençons par ceci : si tu prends deux nombres réels, $a$ et $b$, que signifie pour toi 'être dense' si on essayait de les traduire en termes de distance ?"*
- **Moi** : *"Ça veut dire que la distance entre eux peut être rendue aussi petite qu'on veut, mais qu'il y aura toujours un rationnel entre les deux ?"*
- **Gemini** : *"Exactement. Maintenant, si tu devais construire ce rationnel entre $a$ et $b$, quel outil mathématique utiliserais-tu pour 'découper' l'intervalle $[a, b]$ ?"*
- **Moi** : *"La division décimale ? Ou peut-être un développement en fraction continue ?"*
- **Gemini** : *"Tu chauffes. Regarde ce qui se passe si on multiplie par un entier assez grand..."*

Vous voyez la différence ? Je ne suis plus en train de lire une démonstration ; je suis en train de la construire. À chaque réponse de l'IA, je suis forcé de mobiliser mon intuition et, surtout, de l’exprimer clairement par écrit. Si je me trompe, l'IA ne se contente pas de me corriger : elle me renvoie une question qui met en lumière ma faille logique.

*La Méthode Liouaï, c’est transformer l'IA en miroir de sa propre réflexion. C’est passer de la consommation passive à une posture intellectuelle active.*

## Comprendre la densité

Après ce dialogue, la densité n'était plus une abstraction théorique, mais une évidence visuelle. Voici comment je la comprends aujourd'hui :

Imaginez la droite réelle comme une corde. Les nombres irrationnels sont comme des trous microscopiques qui parsèment cette corde. La densité des rationnels signifie que, si vous prenez une loupe pour examiner le moindre petit segment de cette corde, aussi minuscule soit-il, vous finirez toujours par tomber sur un point rationnel. C’est ce que signifie le théorème : vous ne pouvez jamais être "perdu" dans les irrationnels sans qu'un rationnel ne soit là, à portée de main, pour vous ancrer. Le rationnel est le "point de repère" qui empêche les irrationnels de s'évaporer dans le vide. Saisir cette signification nous permet d’avancer dans la compréhension de la structure de la droite réelle. Elle ouvre la porte aux notions suivantes, comme les suites de rationnels, permettant d’approximer un irrationnel.

Pour ancrer cette compréhension, j'ai codé une petite simulation. Pouvoir expliquer, par l’analogie, un concept délicat et sa preuve est signe d’assimilation. Construire un exemple numérique par le code, c’est une expérience supplémentaire. Ainsi, l'idée de la simulation est simple : choisir deux nombres réels au hasard et chercher un rationnel entre les deux par dichotomie.

```python
from fractions import Fraction
import random

def trouver_rationnel_entre(x, y):
    """
    Trouve un rationnel r = p/q tel que x < r < y.
    On utilise le fait qu'il existe un entier q tel que 1/q < (y - x).
    """
    delta = y - x
    q = int(1 / delta) + 1
    # On cherche p tel que p/q > x => p > x*q
    p = int(x * q) + 1
    return Fraction(p, q)

# Exemple : deux nombres très proches
a = 0.3333333333333333
b = 0.3333333333333334
rationnel = trouver_rationnel_entre(a, b)
print(f"Intervalle : [{a}, {b}]")
print(f"Rationnel trouvé : {rationnel} = {float(rationnel)}")
```

> **Note pour les puristes :**
> En informatique, nous ne manipulons que des rationnels. Ma simulation ne prouve donc pas la densité de $\mathbb{Q}$ dans $\mathbb{R}$ — une preuve qui nécessite la complétude de $\mathbb{R}$. Elle illustre cependant la densité de $\mathbb{Q}$ dans $\mathbb{Q}$ : la preuve que, dans notre espace de calcul, il n'existe pas de 'plus petit rationnel' entre deux autres.

Le code ci-dessus illustre la 'mécanique de la densité'. Même si ma machine est limitée par sa représentation des nombres, elle reproduit à l'infini cette propriété : il existe toujours un rationnel, peu importe la finesse de mon zoom. C'est cette invariance, cette capacité à toujours subdiviser, qui fait toute la puissance de la densité.

## Le savoir n'est pas un monument, c'est un dialogue

Finalement, si mon "combat" avec la densité des rationnels m'a appris une chose, c'est que l'apprentissage solitaire est un piège. Pendant des mois, j'ai cru que mon blocage était une fatalité, un signe que je n'avais pas "l'esprit mathématique". Que c’est trop difficile. J'avais tort. Ce n'était pas une limite de mon intelligence, mais une limite de mon outil de pensée.

En remplaçant la lecture passive par le dialogue socratique, j'ai compris que **les mathématiques ne sont pas un monument que l'on contemple de l'extérieur, mais un dialogue que l'on construit de l'intérieur.**

La méthode **Liouaï** n'est pas une recette miracle pour apprendre plus vite ; c'est un changement de posture. C'est accepter d'être celui qui pose la question, celui qui doute, et celui qui se laisse guider par l'IA pour redouvrir, pas à pas, la logique derrière l'abstraction. Et inversement.

Aujourd'hui, ce vertige qui me paralysait devant mes manuels est devenu mon terrain de jeu. Je ne cherche plus à "contenir" le savoir ; je cherche à le faire dialoguer.

### Et vous, quel est le concept qui vous donne le vertige en ce moment ?

Si vous souhaitez explorer les mathématiques avec cette approche, ou si vous voulez recevoir mes prochaines notes de laboratoire où je déconstruis d'autres notions complexes, je vous invite à rejoindre la communauté Liouaï. Ensemble, nous ferons du "Learn It Yourself" une véritable aventure intellectuelle.
