# Markdown with TeX script
# Requires internet connection
# By Filipe Chagas (filipe.ferraz0@gmail.com)
# sep 2020

import requests
import os
import sys

def download_gif(dest_fn: str, txt: str):
    print(f'downloading {dest_fn}...')

    with open(dest_fn, 'wb') as handle:
            response = requests.get('https://latex.codecogs.com/gif.latex?{' + txt + '}', stream=True)

            if not response.ok:
                raise Exception('Invalid Tex:\n' + txt)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

def process_tex_code(txt: str) -> str:
    txt = ' '.join(txt.split('\n'))
    txt = ' '.join(txt.split('\t'))
    return txt

def process_md_text(md_text: str, imgdir_root) -> str:
    md_text_result = '' #output text
    current_tex = '' 
    inside_tex = False

    image_counter = 0
    i = 0
    while i < len(md_text):
        char = md_text[i]

        if i != len(md_text)-1: #se ainda houver um próximo caractere
            next_char = md_text[i+1]

            #replace '\$' with '$' and jump
            if char == '\\' and next_char == '$':
                md_text_result += '$'
                i += 2
                continue

        if char == '$': #beginning or ending of a TEX code
            if inside_tex == False:
                #set state
                inside_tex = True
            else:
                #download gif with the formula
                image_fn = os.path.join(imgdir_root, f'tex{image_counter}.gif')
                image_counter += 1
                download_gif(image_fn, process_tex_code(current_tex))
                
                #append image to the md
                md_text_result += f' ![tex{image_counter}]({image_fn}) '
                
                #reset states
                current_tex = ''
                inside_tex = False
        
        else: 
            if inside_tex == False: #not inside a TEX code
                md_text_result += char 
            else: #inside a TEX code
                current_tex += char

        i += 1

    return md_text_result


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    imgdir_root = sys.argv[3]

    if not os.path.exists(imgdir_root):
        os.mkdir(imgdir_root)
    elif os.path.isfile(imgdir_root):
        raise Exception(f'{imgdir_root} is not a directory')

    if not os.path.exists(input_filename) or not os.path.isfile(input_filename):
        raise Exception(f'Invalid origin-file name ({input_filename})')

    print('=== Markdown with TeX ===')
    print('By Filipe Chagas (filipe.ferraz0@gmail.com)')
    print('sep 2020')
    print('** Requires internet connection **')
    print('=========================\n')

    print('loading input file...')
    with open(input_filename, 'r') as input_file:
        print('processing markdown...')
        output_file_txt = process_md_text(input_file.read(), imgdir_root)
        
        print('writing output file...')
        with open(output_filename, 'w') as output_file:
            output_file.write(output_file_txt)

    print('done!')

