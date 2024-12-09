import xml.etree.ElementTree as ET

# Define paths for input and output files
lint_file = 'linting-report.txt'
coverage_file = 'cobertura-report.xml'

def create_cobertura_report():
    # Create root XML element for Cobertura
    root = ET.Element("coverage", version="1.9")
    package = ET.SubElement(root, "package", name="cloudformation-templates")

    # Open the linting report and process each line
    with open(lint_file, 'r') as f:
        for line in f.readlines():
            # Each line in the format: template.yaml:3:warning
            parts = line.strip().split(":")
            if len(parts) < 3:
                continue  # Skip malformed lines
            file_name, line_number, issue_type = parts[0], parts[1], parts[2]

            # Add file, line info to the Cobertura XML
            file_element = ET.SubElement(package, "file", name=file_name)
            ET.SubElement(file_element, "line", number=line_number, hits="1", branch="false")

    # Write the XML tree to the output file
    tree = ET.ElementTree(root)
    tree.write(coverage_file)

if __name__ == "__main__":
    create_cobertura_report()
