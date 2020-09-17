# Markdown with TeX

A small tool to add tex formulas to markdown files

By Filipe Chagas

sep 2020

## How to use

### Writing Markdown with TeX
* Write a Markdown file. 
* Place TeX expressions between dollar signs (**"$"**). 
* Do not use double dollar signs (**"$$"**) to centralize the formulas, this feature is not available.
* If you don't want a dollar sign to be interpreted as the beginning or end of a TeX expression, put a forward slash (**"\\$"**).

### Processing the Markdown file
Use the **md_tex.py** script to process the Markdown you wrote. This script will replace all TeX expressions with images. This script requires an internet connection.

You must pass three arguments to the script: (1) the name of the input file, (2) the name of the output file and (3) the name of the directory where the images will be.

```sh
python md_tex.py input_filename output_filename image_dir
```

**The output file must be created in the current working directory. Paths to the output file with sub or super directories are not allowed.**

See usage example in **src/sample**.
