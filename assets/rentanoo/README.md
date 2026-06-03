# Assets Rentanoo — Portfolio

## Fichiers en production (captures réelles)

| Fichier | Écran | Pilier | Usage page |
|---------|--------|--------|------------|
| `01-catalog-search-display.png` | Accueil + recherche dates | Réservation en ligne | Hero, galerie |
| `02-booking-confirmation-display.png` | Modal confirmation réservation | Réservation en ligne | Hero (centre), galerie |
| `03-vehicle-detail-display.png` | Fiche véhicule + CTA Réserver | Réservation en ligne | Hero, galerie |

Versions :
- `*-display.png` — affichage web (~900px)
- `*-thumb.png` — vignettes légères
- `*.png` (sans suffixe) — lightbox / qualité max (~1400px)

## Captures à ajouter (noms cibles)

Déposer les PNG dans ce dossier avec ces noms exacts :

| Fichier cible | Écran à capturer | Pilier |
|---------------|------------------|--------|
| `04-agency-planning.png` | Planning / calendrier agence | CRM & Exploitation |
| `05-digital-edl-mobile.png` | État des lieux mobile (départ ou retour) | CRM & Exploitation |
| `06-fleet-maintenance.png` | Maintenance, stock ou rapport flotte | Gestion de flotte |

Après ajout, régénérer les variantes :

```bash
cd assets/rentanoo
for name in 04-agency-planning 05-digital-edl-mobile 06-fleet-maintenance; do
  sips -Z 1400 "${name}.png" --out "${name}.png"
  sips -Z 900 "${name}.png" --out "${name}-display.png"
  sips -Z 480 "${name}.png" --out "${name}-thumb.png"
done
```

Les placeholders de la page disparaîtront automatiquement si les fichiers `-display.png` existent.

## Conseils capture

- Fenêtre navigateur propre (pas d’extensions visibles)
- Données réalistes mais anonymisées
- Ratio ~16:9 ou capture fenêtre complète
- Export PNG ; le script `sips` génère les tailles web
