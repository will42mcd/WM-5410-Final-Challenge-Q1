from PIL import Image

# load image and return list of pixel values
def get_pixels(image_name):
    with Image.open(image_name) as im:
        im = im.convert("RGB")
        pixels = list(im.getdata())
    return pixels

# convert a string of text to binary and return binary
def text_to_binary(text):
    binary_list = []
    for i in text:
        asc_value = ord(i)
        binary_value = format(asc_value, "08b")
        binary_list.append(binary_value)
    binary_str = ''.join(binary_list) + '1111111111111110' # < delimiter to signal stop decoding
    return binary_str

# encodes the message into the pixels and returns encoded pixels 
def encode_image(pixels, binary_str):
    binary_index = 0
    encoded_pixels = []
    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary_str):
            r = (r & ~1) | int(binary_str[binary_index])  # Modify LSB of red
            binary_index += 1
        if binary_index < len(binary_str):
            g = (g & ~1) | int(binary_str[binary_index])  # Modify LSB of green
            binary_index += 1
        if binary_index < len(binary_str):
            b = (b & ~1) | int(binary_str[binary_index])  # Modify LSB of blue
            binary_index += 1
        encoded_pixels.append((r, g, b))
    encoded_pixels.extend(pixels[len(encoded_pixels):])  # Append remaining unchanged pixels
    return encoded_pixels

# puts the new data into a new image and saves it
def image_reconstruction(pixels, out_image_name):
    image = Image.new("RGB", (360,360), color=(255, 255, 255))
    image.putdata(pixels)
    image.save(out_image_name)

# Contverts binary back to string
def binary_to_text(binary):
    chars = []
    for i in range(0, len(binary), 8):
        char = binary[i:i + 8]  
        chars.append(char)     

    decoded_text = []
    for char in chars:
        if char != '11111110': 
            ascii_value = int(char, 2)
            decoded_text.append(chr(ascii_value)) 
    return ''.join(decoded_text)

# extracts the Least significant Bit from pixels before delimiter
def decode_image(image_name):
    pixels = get_pixels(image_name)
    binary_text = ''
    for pixel in pixels:
        for value in pixel:
            binary_text += str(value & 1)
            if binary_text[-16:] == '1111111111111110': 
                return binary_to_text(binary_text[:-16])
    return binary_to_text(binary_text)
