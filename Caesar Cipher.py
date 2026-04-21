def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    # If decrypting, reverse the shift
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Preserve case
            start = ord('A') if char.isupper() else ord('a')
            # Shift character
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            # Keep spaces/symbols unchanged
            result += char

    return result


# Example usage
message = "Hello World"
shift = 3

encrypted = caesar_cipher(message, shift, "encrypt")
decrypted = caesar_cipher(encrypted, shift, "decrypt")

print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)