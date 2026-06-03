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

**Important :** il suffit d’uploader le fichier de base (ex. `04-agency-planning.png`).  
La page charge automatiquement ce fichier ; les variantes `-display` et `-thumb` sont optionnelles.

Les placeholders disparaissent dès que `04-agency-planning.png`, `05-digital-edl-mobile.png` ou `06-fleet-maintenance.png` est présent dans ce dossier.

Variantes optionnelles (macOS) :

```bash
cd assets/rentanoo
for name in 04-agency-planning 05-digital-edl-mobile 06-fleet-maintenance; do
  [ -f "${name}.png" ] || continue
  sips -Z 900 "${name}.png" --out "${name}-display.png"
  sips -Z 480 "${name}.png" --out "${name}-thumb.png"
done
```

## Conseils capture

- Fenêtre navigateur propre (pas d’extensions visibles)
- Données réalistes mais anonymisées
- Ratio ~16:9 ou capture fenêtre complète
- Export PNG ; le script `sips` génère les tailles web
