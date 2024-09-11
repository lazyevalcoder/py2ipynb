from py2ipynb import convert_py_to_ipynb, add_cell, remove_cell, notebook_info

convert_py_to_ipynb('helloworld.py')  # First, convert the .py to .ipynb

add_cell('helloworld.ipynb', '# New Markdown Cell', cell_type='markdown', position=0)  # Add at the top

add_cell('helloworld.ipynb', 'print("Hello Babe")', cell_type='code', position=1)  # Add at the top

add_cell('helloworld.ipynb', 'print("This cell will be deleted")', cell_type='markdown', position=2)  # Add at the top

remove_cell('helloworld.ipynb', 2)

print(notebook_info('helloworld.ipynb'))
