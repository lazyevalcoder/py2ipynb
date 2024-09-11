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

#Edit a Specific Cell
def edit_cell(nb_file, index, new_content):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    if 0 <= index < len(nb.cells):
        nb.cells[index].source = new_content

    with open(nb_file, 'w') as f:
        nbformat.write(nb, f)

#Move a Cell
def move_cell(nb_file, old_index, new_index):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    if 0 <= old_index < len(nb.cells) and 0 <= new_index < len(nb.cells):
        nb.cells.insert(new_index, nb.cells.pop(old_index))

    with open(nb_file, 'w') as f:
        nbformat.write(nb, f)

#Cell Type Conversion
def convert_cell_type(nb_file, index, target_type):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    if 0 <= index < len(nb.cells):
        if target_type == 'code' and nb.cells[index].cell_type == 'markdown':
            nb.cells[index] = nbformat.v4.new_code_cell(source=nb.cells[index].source)
        elif target_type == 'markdown' and nb.cells[index].cell_type == 'code':
            nb.cells[index] = nbformat.v4.new_markdown_cell(source=nb.cells[index].source)

    with open(nb_file, 'w') as f:
        nbformat.write(nb, f)

#Export Notebook as Plain Python Script
def export_to_py(nb_file, py_file):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    with open(py_file, 'w') as f:
        for cell in nb.cells:
            if cell.cell_type == 'code':
                f.write(cell.source + '\n\n')

#Search for a Cell by Content
def search_cell(nb_file, search_term):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    matches = []
    for i, cell in enumerate(nb.cells):
        if search_term in cell.source:
            matches.append((i, cell.source))

    return matches

#Merge Multiple Notebooks
def merge_notebooks(nb_files, output_file):
    new_nb = nbformat.v4.new_notebook()

    for nb_file in nb_files:
        with open(nb_file, 'r') as f:
            nb = nbformat.read(f, as_version=4)
            new_nb.cells.extend(nb.cells)

    with open(output_file, 'w') as f:
        nbformat.write(new_nb, f)

#Clear All Outputs
def clear_outputs(nb_file):
    with open(nb_file, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.outputs = []

    with open(nb_file, 'w') as f:
        nbformat.write(nb, f)
