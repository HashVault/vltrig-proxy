#!/usr/bin/env python3

import gzip
import sys
import os


def main():
    if len(sys.argv) < 2:
        input_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'webui', 'index.html')
    else:
        input_path = sys.argv[1]

    if len(sys.argv) < 3:
        output_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'webui', 'webui_html.h')
    else:
        output_path = sys.argv[2]

    try:
        with open(input_path, 'rb') as f:
            raw = f.read()
    except FileNotFoundError:
        print(f'Error: {input_path} not found', file=sys.stderr)
        return 1

    compressed = gzip.compress(raw, compresslevel=9)

    lines = []
    for i in range(0, len(compressed), 16):
        chunk = compressed[i:i + 16]
        hex_bytes = ', '.join(f'0x{b:02x}' for b in chunk)
        lines.append(f'    {hex_bytes}')

    array_body = ",\n".join(lines)

    header = (
        "#ifndef XMRIG_WEBUI_HTML_H\n"
        "#define XMRIG_WEBUI_HTML_H\n"
        "\n"
        "#include <cstddef>\n"
        "\n"
        "namespace xmrig {\n"
        "\n"
        "static const unsigned char kWebUiHtml[] = {\n"
        + array_body + "\n"
        "};\n"
        "\n"
        "static const size_t kWebUiHtmlSize = sizeof(kWebUiHtml);\n"
        "\n"
        "} // namespace xmrig\n"
        "\n"
        "#endif // XMRIG_WEBUI_HTML_H\n"
    )

    tmp_path = output_path + '.tmp'
    with open(tmp_path, 'w') as f:
        f.write(header)
    os.replace(tmp_path, output_path)

    ratio = (1 - len(compressed) / len(raw)) * 100 if raw else 0
    print(f'Web UI: {len(raw)} -> {len(compressed)} bytes ({ratio:.1f}% compression)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
