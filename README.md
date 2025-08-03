# 🎨 Hirst Dot Painting Generator with Python Turtle

A fun and colorful Python project that uses the `turtle` module to generate a grid of colored dots inspired by Damien Hirst's dot artwork. This is a beginner-friendly creative coding exercise that demonstrates basic concepts in turtle graphics, loops, color handling, and randomness.

![Python](https://img.shields.io/badge/Built%20With-Python-blue?style=flat-square)
![Art](https://img.shields.io/badge/Project-Hirst%20Dot%20Art-pink?style=flat-square)
![Level](https://img.shields.io/badge/Difficulty-Beginner-green?style=flat-square)

---

## 🖌️ Project Overview

This script creates a 10x10 grid of colored dots using the `turtle` module. Each dot is randomly colored from a predefined palette of RGB tuples.

It mimics the modern art style made popular by **Damien Hirst**, known for using vibrant, colorful, uniform dots in a grid layout.

---

## 🧱 File Structure

---

## 🎯 Features

- Grid of 100 colored dots (10 rows x 10 columns)
- Each dot is 10 pixels in size and spaced evenly
- Dot colors are randomly chosen from a curated color palette
- Uses RGB mode with `colormode(255)` from `turtle`

---

## 🐢 How It Works

- `turtle` is used for drawing
- `penup()` prevents lines between dots
- A `for` loop iterates 100 times to draw 100 dots
- After every 10 dots, the turtle moves up and resets its horizontal position

---

## 🎨 Color Palette

Colors are stored as a list of RGB tuples, e.g.:

```python
(197, 13, 34), (232, 227, 5), (44, 211, 74), ...

