FULLIMAGE_PATH = "/Users/macbook/proxmark3/armsrc/obj/fullimage.elf"
IDENTIFIER = "Keysrus"
OFFSET = 0x1FFF0

def embed_identifier():
    with open(FULLIMAGE_PATH, "rb+") as file:
        file.seek(OFFSET)
        file.write(IDENTIFIER.encode("utf-8"))
        print(f"Successfully embedded '{IDENTIFIER}' at offset {OFFSET}.")

embed_identifier()
