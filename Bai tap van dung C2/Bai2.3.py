
import sys
import xml.dom.minidom
from xml.parsers.expat import ExpatError


def _usage():
    print("Usage: python Bai2.3.py [xml_file]")


def main():
    # Chấp nhận tên file từ argv, mặc định là sample.xml
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

    # In ra tên node tài liệu và tag name của phần tử gốc
    print(doc.nodeName)
    print(doc.documentElement.tagName)
    return 0
if __name__ == "__main__":
    sys.exit(main())