# [Challenges](https://github.com/blaketyro/challenges)

Code challenges from various websites solved in various languages.

The languages include:

-   [Python](/Python) - [python.org](https://www.python.org/) (version 3.11)
-   [Rust](/Rust) - [rust-lang.org](https://www.rust-lang.org/) (version 1.70)

The websites include:

-   [LeetCode](https://leetcode.com/problemset/all/) - [leetcode.com](https://leetcode.com/)
-   [Project Euler](https://projecteuler.net/archives) - [projecteuler.net](https://projecteuler.net/)

## Repo Structure

This repo is organized into folders for languages, which contain subfolders for websites, which contain individual files
for challenges, as follows:

> -   [/README.md](/README.md)
> -   /language1 folder
>     -   /website1 folder
>         -   /challenge1.ext file
>         -   /challenge2.ext file
>         -   ...
>     -   /website2 folder
>         -   /challenge1.ext file
>         -   /challenge2.ext file
>         -   ...
>     -   ...
> -   /language2 folder
>     -   ...

(Other project and language specific setup files and folders are not shown.)

A comment that links to the challenge should be at the top of every challenge file. Multiple solutions for the same
challenge in the same language should be in the same file.

For recognizability, language folder names are capitalized/stylized to match the language's branding, but website folder
names are lowercase since not all language project structures allow uppercase in subfolder names. The relative path to
the same challenge file across languages should be the same except for the file extension.
