import sys
import xml.dom.minidom
from xml.parsers.expat import ExpatError


def _get_text(node_list):
    """Return text content for the first node in node_list or empty string."""
    if not node_list:
        return ""
    node = node_list[0]
    if node is None or node.firstChild is None:
        return ""
    return node.firstChild.data.strip()


def _usage():
    print("Usage: python Bai2.4.py [xml_file]")


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "sample.xml"
    try:
        doc = xml.dom.minidom.parse(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        _usage()
        return 1
    except ExpatError as e:
        print(f"Failed to parse XML ({filename}): {e}", file=sys.stderr)
        return 2

    staffs = doc.getElementsByTagName("staff")
    if not staffs:
        print("No <staff> elements found.")
        return 0

    for staff in staffs:
        name = _get_text(staff.getElementsByTagName("name"))
        salary = _get_text(staff.getElementsByTagName("salary"))
        print(f"Name: {name}")
        print(f"Salary: {salary}")

    return 0


if __name__ == "__main__":
    sys.exit(main())