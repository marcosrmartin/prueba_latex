# Moving Target Defense

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![GitHub](https://img.shields.io/github/license/erseco/moving_target_defense.svg)](https://github.com/erseco/moving_target_defense/blob/master/LICENSE)
[![LaTeX Build](https://travis-ci.com/erseco/moving_target_defense.svg?branch=master)](https://travis-ci.com/erseco/moving_target_defense)
[![Docker Build](https://github.com/erseco/moving_target_defense/workflows/Docker%20Image%20CI/badge.svg)
[![Python Tests](https://github.com/erseco/moving_target_defense/workflows/Python%20package/badge.svg)


## Sistema de ciberdefensa dinámica basada en tmos evolutivos para la prevención de ataques informáticos

Now also in paper form! To be published soon in EvoApplications.

## Abstract

Además de realizar una labor determinada de forma eficiente, los servicios informáticos deben ser capaces de evitar los ataques y de detectar los que haya. Una técnica de defensa consiste en convertirse en un "objetivo móvil", que varíe el perfil de forma que los atacantes no lo reconozcan.

Mediante algoritmos evolutivos trataremos de configurar diferentes servicios de forma que se maximice la diversidad, a la vez que se optimice la seguridad y las prestaciones.

## Contenido
 
- Memoria: [pdf](../../releases/download/1.0.0/project.pdf)
- Presentación: [pdf](../../releases/download/1.0.0/slides.pdf)
- Código: [code](../../tree/master/code)
 
### Autor: Ernesto Serrano Collado
### Tutor: Juan Julián Merelo Guervós

Memoria realizada con LaTeX, para generar el archivo PDF introducir las siguientes órdenes:

```
sudo apt-get -qq update && sudo apt-get install -y --no-install-recommends texlive-fonts-recommended texlive-latex-extra texlive-fonts-extra dvipng texlive-latex-recommended texlive-bibtex-extra biber
make
```

*Memoria y Presentación* liberada bajo la licencia **Creative Commons Attribution-ShareAlike 4.0 International**.

*Código* liberado bajo licencia **GNU GENERAL PUBLIC LICENSE Version 3**.
