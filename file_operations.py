from caesar_ciper import encrypt, decrypt

def process_file(input_path, output_path, shift, mode='encrypt'):
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
    result = encrypt(content, shift) if mode == 'encrypt' else decrypt(content, shift)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(result)
