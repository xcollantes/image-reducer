"""Utility to compress and reduce images."""

import os 
import locale 
import logging 
from PIL import Image, ImageFilter 

locale.setlocale(locale.LC_ALL, "")
logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():
    image_file: Image = Image.open(IMAGE)
  
    basename: str = os.path.basename(IMAGE)
    save_path: str = os.path.join(
                os.path.dirname(os.path.abspath(IMAGE)),
                os.path.splitext(basename)[0] + "_optimized" 
                + os.path.splitext(basename)[1])
        
    image_file.save(save_path, quality=20)

    logging.info("Saved to %s", save_path)    
    logging.info("W: %s H: %s", image_file.width, image_file.height)  
    
    input_size: int = os.path.getsize(IMAGE)
    result_size: int = os.path.getsize(save_path)
    logging.info("Image reduced from %s to %s [%s]", f"{input_size:n} B", 
        f"{result_size:n} B", 
        f"{(input_size - result_size) / input_size:n}%")


if __name__ == "__main__":
    main()
