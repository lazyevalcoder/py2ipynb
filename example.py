from py2ipynb import (
    convert_py_to_ipynb, add_cell, remove_cell, edit_cell, move_cell,
    convert_cell_type, export_to_py, search_cell, merge_notebooks, clear_outputs, notebook_info
)

# Step 1: Convert Python file to Jupyter Notebook
convert_py_to_ipynb('helloworld.py')

# Step 2: Add new markdown and code cells
add_cell('helloworld.ipynb', '# This is a new markdown cell', cell_type='markdown', position=0)
add_cell('helloworld.ipynb', 'print("This is a new code cell")', cell_type='code', position=1)

# Step 3: Edit the first code cell (at position 1)
edit_cell('helloworld.ipynb', 1, 'print("Edited the first code cell")')

# Step 4: Move the second cell (index 1) to the top (index 0)
move_cell('helloworld.ipynb', 1, 0)

# Step 5: Convert the first cell from code to markdown
convert_cell_type('helloworld.ipynb', 0, 'markdown')

# Step 6: Search for a term in the notebook (e.g., "print")
search_results = search_cell('helloworld.ipynb', 'print')
print(f"Search results for 'print': {search_results}")

# Step 7: Merge two notebooks into one (e.g., helloworld.ipynb and another_notebook.ipynb)
merge_notebooks(['helloworld.ipynb', 'another_notebook.ipynb'], 'merged_notebook.ipynb')

# Step 8: Clear all outputs in the notebook (reset it for sharing)
clear_outputs('helloworld.ipynb')

# Step 9: Export the notebook back to a Python script
export_to_py('helloworld.ipynb', 'exported_helloworld.py')

# Step 10: Display notebook info (total cells, markdown, and code cells count)
print(notebook_info('helloworld.ipynb'))
