from encoding_functions import *

def main():
    pixels = get_pixels("nebula.png")
    while True:
        user_mode = input("Please enter mode (E)ncode or (D)ecode:  ")
        if user_mode not in ['E', 'D']:
            print("Please enter correct input: E or D")
            continue
        elif user_mode == 'E':
            user_text = input("Please Enter the text to encode on an image:\n")
            user_binary = text_to_binary(user_text)
            encoded_pixels = encode_image(pixels, user_binary)
            print('Encoding Complete')
            image_reconstruction(encoded_pixels, 'encoded_image.png')
        elif user_mode == 'D':
            try:
                message = decode_image('encoded_image.png')
                print("Found:   ", message)
            except FileNotFoundError:
                print("There is no file to decode...")
                continue



if __name__ == "__main__":
    main()