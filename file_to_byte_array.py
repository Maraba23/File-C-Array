def generate_byte_array(file_path, output_path):
    with open(file_path, 'rb') as f:
        byte_array = f.read()

    with open(output_path, 'w') as f:
        f.write('#include <stdint.h>\n\n')
        f.write('const uint8_t executable_array[] = {\n    ')
        line_length = 0
        for byte in byte_array:
            f.write(f'0x{byte:02x}, ')
            line_length += 1
            if line_length == 12:
                f.write('\n    ')
                line_length = 0
        f.write('\n};\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <path_to_executable> <output_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_path = sys.argv[2]
    generate_byte_array(file_path, output_path)
