# Registre Génération 10

Planificateur d'élevage pour Dofus 3.7 : il guide pas à pas vers les succès de naissance des générations 2 à 10
pour les dragodindes, les muldos et les volkornes (croisements, captures, nombre d'accouplements estimé).

Site de fan non officiel, non affilié à Ankama.

## Structure

- `template.html` : la page (HTML, CSS et JS), avec un emplacement `/*__DATA__*/` pour les données.
- `montures.json` : montures par famille, génération, couleurs et recettes de croisement.
- `build.py` : assemble les pages finales.
- `docs/index.html` : version autonome servie par GitHub Pages (générée).
- `index.html` : version pour l'artifact claude.ai, sans doctype (générée).

## Mettre à jour le site

```sh
python build.py
git add -A
git commit -m "Mise à jour"
git push
```

GitHub Pages republie `docs/` automatiquement après chaque push.

## Sources

- Recettes de croisement : [dragodinde.fr](https://dragodinde.fr/)
- Noms officiels des montures : [DofusDB](https://dofusdb.fr/)
- Mécaniques : [Guide de l'éleveur, édition 2026](https://www.dofuspourlesnoobs.com/guide-de-l-eleveur.html)
