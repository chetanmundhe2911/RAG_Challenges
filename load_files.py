# Load the files
def load_companies(file1, file2):
    companies = []
    for file_path in [file1, file2]:
        with open(file_path, 'r') as file:
            for line in file:
                companies.append(ast.literal_eval(line.strip()))
    return companies
