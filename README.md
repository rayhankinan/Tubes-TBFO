# Tubes-TBFO
Tugas Besar IF2124 Teori Bahasa Formal dan Otomata Compiler Bahasa Python

## Table of Contents
* [General Information](#general-information)
* [Structures](#structures)
* [Setup and Usage](#setup-and-usage)

## General Information
Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat
dieksekusi oleh mesin, terdapat pemeriksaan sintaks atau kompilasi bahasa yang dibuat oleh
programmer. Kompilasi ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer
mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter
maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak
pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai
dilakukanDalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat
dieksekusi oleh mesin, terdapat pemeriksaan sintaks atau kompilasi bahasa yang dibuat oleh
programmer. Kompilasi ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer
mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter
maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak
pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai
dilakukan.  
<br />
Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan kompilasi. Sudah
sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler
dengan performa yang tinggi. Terdapat CFG, CNF, 2NF, 2LF, dll untuk grammar yang
dapat digunakan, dan terdapat LL(0), LL(1), CYK, Earley’s Algorithm, LALR, GLR, Shift-reduce,
SLR, LR(1), dll untuk algoritma yang dapat digunakan untuk melakukan parsing.

## Structures
```bash
.
    file.txt
    file_processing.py
    grammar.txt
    grammar_convert.py
    grammar_parser.py
    grammar_processing.py
    parserprogram.py
    README.md
```

## Setup and Usage
1. Clone repository ini menggunakan menggunakan command `git clone https://github.com/rayhankinan/Tubes-TBFO.git`.
2. Ketik source code yang hendak di parsing pada suatu file dengan directory yang sama dengan program `parsingprogram.py`, kemudian save file tersebut.
3. Jalankan program parsing menggunakan command `py parsingprogram.py <source_code>`.