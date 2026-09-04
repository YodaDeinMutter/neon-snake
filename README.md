# neon-snake
Snake-Spiel in Python mit Portal-Wänden und Neon-3D-Look.

# 🐍 Neon Snake

Ein modernes Snake-Spiel in Python mit **Tkinter**, Neon-Optik und einem kleinen Twist:
**Die Wände sind Portale!** 🌀

Wenn die Schlange den Spielfeldrand erreicht, erscheint sie auf der gegenüberliegenden Seite wieder.

---

## ✨ Features

* 🐍 Klassisches Snake-Gameplay
* 🌀 **Portal-Wände** – keine Kollision mit dem Spielfeldrand
* 🌈 Neon-inspirierte Benutzeroberfläche
* 🍎 Animierte/gestylte Früchte
* 🏆 Punktestand und Highscore
* ⏱️ Geschwindigkeit steigt mit zunehmendem Score
* ⏸️ Pause-Funktion
* 🔄 Spiel jederzeit neu startbar
* 🎮 Pfeiltasten und WASD-Unterstützung
* 🖥️ Läuft mit Python und Tkinter
* 🚫 Keine zusätzlichen Python-Pakete erforderlich

---

## 📸 Vorschau

> Screenshot oder GIF des Spiels hier einfügen.

Zum Beispiel:

```text
docs/screenshot.png
```

Du kannst später ein Bild in dein Repository hochladen und diesen Abschnitt entsprechend anpassen.

---

## 🛠️ Voraussetzungen

Du benötigst:

* **Python 3**
* **Tkinter**

Unter vielen Linux-Distributionen ist Tkinter bereits vorhanden.

### Manjaro / Arch Linux

Falls Tkinter fehlt:

```bash
sudo pacman -S tk
```

Prüfen:

```bash
python --version
```

---

## 🚀 Installation

Repository klonen:

```bash
git clone https://github.com/YodaDeinMutter/neon-snake.git```

In das Verzeichnis wechseln:

```bash
cd neon-snake
```

Spiel starten:

```bash
python snake_3d.py
```

Falls dein System `python` nicht verwendet:

```bash
python3 snake_3d.py
```

---

## 🎮 Steuerung

| Taste        | Funktion           |
| ------------ | ------------------ |
| ⬆️ `↑` / `W` | Nach oben          |
| ⬇️ `↓` / `S` | Nach unten         |
| ⬅️ `←` / `A` | Nach links         |
| ➡️ `→` / `D` | Nach rechts        |
| `P`          | Pause / Fortsetzen |
| `R`          | Neue Runde         |
| `Esc`        | Spiel beenden      |

---

## 🌀 Portal-System

Das Spielfeld besitzt keine tödlichen Außenwände.

Wenn die Schlange beispielsweise rechts aus dem Spielfeld herausläuft, erscheint sie links wieder.

```text
        ┌──────────────────┐
        │                  │
        │       🐍 →       │
        │                  │
        └──────────────────┘
                   ↓
              erscheint
              links wieder
```

Dadurch kann die Schlange das gesamte Spielfeld nutzen.

---

## 🏆 Punkte

Für jede gefressene Frucht erhält der Spieler:

```text
+10 Punkte
```

Der aktuelle Punktestand und der beste erreichte Score werden rechts neben dem Spielfeld angezeigt.

Die Geschwindigkeit der Schlange erhöht sich außerdem schrittweise mit dem Score.

---

## 📁 Projektstruktur

```text
neon-snake/
│
├── snake_3d.py
├── README.md
└── LICENSE
```

Optional kannst du später noch einen `docs/`-Ordner für Screenshots hinzufügen:

```text
neon-snake/
│
├── snake_3d.py
├── README.md
├── LICENSE
│
└── docs/
    └── screenshot.png
```

---

## 🔧 Technische Details

Das Spiel wurde vollständig mit Python und Tkinter umgesetzt.

Verwendete Python-Module:

```python
import random
import tkinter as tk
```

Es werden keine externen Python-Bibliotheken benötigt.

Das Spielfeld besteht aus:

```text
20 × 20 Zellen
```

mit einer Zellgröße von:

```text
30 × 30 Pixel
```

Die Benutzeroberfläche verwendet ein eigenes Farbschema und wird vollständig über Tkinter's `Canvas` gezeichnet.

---

## 🎨 Design

Das Spiel verwendet einen dunklen Hintergrund mit leuchtenden Farben:

* 🟢 Neon-Grün für die Schlange
* 🔴 Pink/Rot für die Früchte
* 🔵 Dunkle Blau-Töne für das Spielfeld
* ⚪ Helle Schrift für die Benutzeroberfläche

Das Ziel ist eine Mischung aus klassischem Snake und einem modernen **Cyberpunk/Neon-Look**.

---

## 🐞 Bekannte Einschränkungen

Aktuell handelt es sich um ein kleines Singleplayer-Spiel.

Geplante mögliche Erweiterungen:

* 🔊 Soundeffekte
* 🎵 Hintergrundmusik
* ✨ Partikeleffekte
* 🌟 Animierte Früchte
* 📈 Highscore dauerhaft speichern
* 🏅 Bestenliste
* ⚡ Verschiedene Schwierigkeitsstufen
* 🎨 Mehrere Themes
* 🗺️ Unterschiedliche Maps
* 💣 Hindernisse
* 🍒 Unterschiedliche Fruchttypen
* 🐍 Skins für die Schlange

---

## 💡 Ideen für zukünftige Versionen

### Version 1.1

* Soundeffekte
* verbesserte Animationen
* gespeicherter Highscore

### Version 1.2

* verschiedene Schwierigkeitsgrade
* Hindernisse
* neue Karten

### Version 2.0

* Menüsystem
* mehrere Spielmodi
* zusätzliche Power-Ups
* vollständiges Neon-UI

---

## 📜 Lizenz

Dieses Projekt kann beispielsweise unter der **MIT License** veröffentlicht werden.

---

## 👨‍💻 Autor
Cerzz
dnljung@proton.me

Entwickelt mit **Python ** und **Tkinter**.

Viel Spaß beim Spielen! 🎮

---

⭐ Wenn dir das Projekt gefällt, kannst du dem Repository gerne einen **Star** geben!

