import nbformat

def convert_py_to_ipynb(py_file):
    with open(py_file, 'r') as f:
        code = f.read()

    lines = [l.strip() for l in code.split('\n')]

    imports = [line for line in lines if line.startswith('import ') or line.startswith('from ')]
    other_lines = [line for line in lines if line not in imports]

    nb = nbformat.v4.new_notebook()
    code_cell = nbformat.v4.new_code_cell()
    code_cell.source = '\n'.join(imports + [''] + other_lines)
    nb.cells.append(code_cell)

    with open(py_file.replace('.py', '.ipynb'), 'w') as f:
        nbformat.write(nb, f)

# Add a new cell (as a utility function)
def add_cell(nb_file, content, cell_type='code', position=-1):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    new_cell = nbformat.v4.new_code_cell() if cell_type == 'code' else nbformat.v4.new_markdown_cell()
    new_cell.source = content

    if position == -1:  # Append at the end
        nb.cells.append(new_cell)
    else:
        nb.cells.insert(position, new_cell)

    with open(nb_file, 'w') as f:
        nbformat.write(nb, f)

# Remove a specific cell
def remove_cell(nb_file, index):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    if 0 <= index < len(nb.cells):
        nb.cells.pop(index)

    with open(nb_file, 'w') as f:
        nbformat.write(nb, f)

# Get notebook info: number of cells, types, etc.
def notebook_info(nb_file):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    num_cells = len(nb.cells)
    code_cells = sum(1 for cell in nb.cells if cell.cell_type == 'code')
    markdown_cells = sum(1 for cell in nb.cells if cell.cell_type == 'markdown')

    print(f"Notebook: {nb_file}")
    print(f"Total Cells: {num_cells}")
    print(f"Code Cells: {code_cells}")
    print(f"Markdown Cells: {markdown_cells}")

# Example Usage
#convert_py_to_ipynb('helloworld.py')  # First, convert the .py to .ipynb
#add_cell('helloworld.ipynb', '# New Markdown Cell', cell_type='markdown', position=0)  # Add at the top
#notebook_info('helloworld.ipynb')  # Get info about the notebook
