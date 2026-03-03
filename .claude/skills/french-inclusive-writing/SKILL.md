---
name: french-inclusive-writing
description: Apply inclusive French writing standards to any task that generates, edits, rewrites, translates, or reviews French content (Markdown pages, docs, posts, announcements, UI copy, emails). Trigger whenever output contains French sentences, even if the user does not explicitly ask for inclusive writing. Enforce epicene wording first, systematic feminine forms for roles, controlled midpoint use, double flexion in greetings/solemn passages, proximity agreement, and readability safeguards.
---

# French Inclusive Writing

Produire ou réviser tout texte français en écriture inclusive, fluide et lisible, sans sacrifier la clarté.

## Workflow

1. Détecter toute sortie en français.
- Activer ce skill dès qu'un texte est rédigé, édité, traduit ou reformulé en français.
- Appliquer ces règles même si la demande ne mentionne pas explicitement l'écriture inclusive.

2. Choisir d'abord une formulation épicène.
- Préférer les termes neutres et englobants avant le point médian.
- Exemples: `le personnel` plutôt que `les employés`, `la communauté étudiante` plutôt que `les étudiants`.

3. Féminiser systématiquement métiers, titres et fonctions.
- Employer les formes féminines: `la chercheuse`, `la cheffe de projet`, `la directrice`.
- Si la personne visée est connue, respecter son genre réel.

4. Utiliser le point médian uniquement si nécessaire.
- Structure: radical + terminaison masculine + `·` + terminaison féminine.
- Exemples: `artisan·es`, `prêt·e`, `motivé·es`.
- Éviter les formes lourdes comme `la·le directeur·rice`; reformuler en terme collectif (`la direction`) quand possible.

5. Utiliser la double flexion pour les salutations et passages solennels.
- Exemples: `Bonjour à toutes et à tous`, `Chères participantes et chers participants`.

6. Appliquer l'accord de proximité.
- Accorder l'adjectif avec le nom le plus proche dans une énumération.
- Exemple: `Les hommes et les femmes sont contentes`.

7. Vérifier accessibilité, cohérence et lisibilité.
- Limiter la densité de points médians dans les phrases longues (préférer les collectifs).
- Maintenir une convention homogène dans un même paragraphe.
- Ne pas mélanger `étudiant·es` et `étudiants et étudiantes` dans un même paragraphe.

## Transformations de référence

- Métiers
  - Classique: `Le directeur et les ingénieurs.`
  - Inclusif: `La direction et les ingénieur·es.`

- Collectifs
  - Classique: `Les utilisateurs de l'application.`
  - Inclusif: `Les utilisateur·rices de l'application.`

- Neutre
  - Classique: `Les droits de l'homme.`
  - Inclusif: `Les droits humains.`

- Adjectifs
  - Classique: `Ils sont tous motivés.`
  - Inclusif: `Ils et elles sont toutes et tous motivé·es.`

- Accord
  - Classique: `Les hommes et les femmes sont contents.`
  - Inclusif: `Les hommes et les femmes sont contentes.`
