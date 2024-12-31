# Python script to embed "Keysrus" into the firmware
FULLIMAGE_PATH = "fullimage.bin"  # Path to the firmware binary file
IDENTIFIER = "Keysrus"            # Unique identifier
OFFSET = 0x1FFF0                 # Reserved offset near the end of firmware

def embed_identifier():
    try:
        with open(FULLIMAGE_PATH, "rb+") as file:
            file.seek(OFFSET)  # Move to the reserved offset
            file.write(IDENTIFIER.encode("utf-8"))  # Write identifier
            print(f"Successfully embedded '{IDENTIFIER}' at offset {OFFSET}.")
    except FileNotFoundError:
        print(f"Firmware file '{FULLIMAGE_PATH}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

embed_identifier()
