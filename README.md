# The Captcha Cracker
This repository contains my solution to [The Captcha Cracker challenge on HackerRank](https://www.hackerrank.com/challenges/the-captcha-cracker/problem).

There are two python code files in this repository:
1. `extract_templates.py`: goes through the training images and isolates individual characters. The output is a dictionary that maps characters from the alphabet to numpy image arrays containing the characters.
2. `solution.py`: uses the templates extracted with the first code to do exact template matching.