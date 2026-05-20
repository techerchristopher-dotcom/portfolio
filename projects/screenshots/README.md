# Screenshots des projets

Dépose ici les captures d'écran de chaque projet, en respectant la convention de nommage ci-dessous.

## Convention de nommage

```
{slug-projet}-screen-{n}.jpg
```

| Projet | Slug | Exemple |
|---|---|---|
| Tukme | `tukme` | `tukme-screen-1.jpg` |
| Rentanoo | `rentanoo` | `rentanoo-screen-1.jpg` |
| Astra App | `astra` | `astra-screen-1.jpg` |
| TSplus RAG | `tsplus` | `tsplus-screen-1.jpg` |
| Agent Rebecca | `rebecca` | `rebecca-screen-1.jpg` |

## Format recommandé

- **Format** : JPG ou PNG
- **Largeur max** : 1200 px (la galerie redimensionne automatiquement)
- **Ratio** : libre (paysage 16:9 recommandé pour les apps web, portrait pour les apps mobiles)

## Mettre à jour les balises `<img>` dans chaque landing page

Une fois tes screenshots déposés ici, remplace les balises placeholder dans le fichier HTML correspondant.

Exemple dans `projects/tukme.html` :

```html
<!-- AVANT -->
<img src="./screenshots/tukme-screen-1.jpg" alt="[ décris l'écran ]" class="screenshot-img placeholder-img">

<!-- APRÈS -->
<img src="./screenshots/tukme-screen-1.jpg" alt="Tukme — écran d'accueil" class="screenshot-img">
<!-- retire la classe placeholder-img et mets un alt descriptif -->
```

Supprime la classe `placeholder-img` et le commentaire PLACEHOLDER une fois l'image insérée.
