import os
import re

dir_path = os.path.abspath(os.path.dirname(__file__))


# 递归读取某个文件夹下的所有文件
def transfer_all_markdown_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                markdown_content = read_file(path)
                converted_content = convert_latex_to_katex(markdown_content)
                write_file(converted_content, path)


def find_dollar_strings(text):
    pattern = r'/((.+?))/'
    replaced_text = re.sub(pattern, r'\\(\1\\)', text)
    return replaced_text


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# 写入更新后的Markdown文件
def write_file(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)


def replace_underscore(text):
    # 使用正则表达式，匹配不以反斜杠开头的下划线
    return re.sub(r'(?<!\\)_', r'\\_', text)


# 将行内LaTeX公式转换为KaTeX
def replace_inline_latex(match):
    latex_code = match.group(1)
    latex_code = replace_underscore(latex_code)
    return f'\\\({latex_code}\\\)'


# 将LaTeX公式转换为KaTeX格式
def convert_latex_to_katex(markdown_content):
    # 匹配行内LaTeX公式（$...$）
    inline_latex_pattern = re.compile(r'\$(.+?)\$')

    # 替换行内的LaTeX公式
    markdown_content = inline_latex_pattern.sub(replace_inline_latex, markdown_content)

    return markdown_content


transfer_all_markdown_files(dir_path)

