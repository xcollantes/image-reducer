"""Utility to compress and reduce images."""

import os 
import locale 
from absl import app, flags, logging
from PIL import Image

locale.setlocale(locale.LC_ALL, "")
logging.get_absl_handler().setFormatter(None)

FLAGS = flags.FLAGS
flags.DEFINE_string("input", "", "File or directory to compress.  Will not recursively compress.")
flags.DEFINE_integer("quality", 40, "Level of quality for the output image.  Integer between 0 - 100.")
flags.DEFINE_string("append_to_name", "", "Some string to append to filename after compression.")

def main(_):
    input: str = FLAGS.input
    quality: int = FLAGS.quality
    append: str = FLAGS.append_to_name

    original_total: int = 0
    post_process_total: int = 0
    if os.path.isdir(input):
        print("DIRECTORY FOUND")
        for dir, _, files in os.walk(input):
            for file in files:
                original_total, post_process_total = compress_image(
                    os.path.join(dir, file), quality, append)

    else:
        image_original_size, image_post_size = compress_image(input, quality, append)

        original_total += image_original_size
        post_process_total += image_post_size

    logging.info("OVERALL REPORT")
    logging.info("Total batch from %s to %s", f"{original_total:n} B", 
                 f"{post_process_total:n} B")  
    logging.info("Total of %s saved", 
                 f"{(original_total - post_process_total) /  original_total * 100:n}%")


def compress_image(image_path: str, compression_level: int, 
                   append_name: str) -> tuple[int, int]:
    """Input one image path to compress.
    
    Args:
        image_path: Absolute or relative image path. 
        quality: An integer from 0 to 100 to specify image quality.  
        append_name: Some string to add to end of file name to differentiate 
            from original version.  
    
    Returns: 
        Tuple of size in bytes of original and after compressing image.  
    """  
    image_abs_path: str = os.path.abspath(image_path)
    image_file: Image = Image.open(image_abs_path)
  
    append: str = f"_{append_name}" if append_name else ""
    basename: str = os.path.basename(image_abs_path)
    save_path: str = os.path.join(
                os.path.dirname(image_abs_path),
                os.path.splitext(basename)[0] + append
                + os.path.splitext(basename)[1])
        
    image_file.save(save_path, quality=compression_level)

    logging.info("Saved to %s", save_path)    
    logging.info("W: %s H: %s", image_file.width, image_file.height)  
    
    input_size: int = os.path.getsize(image_abs_path)
    result_size: int = os.path.getsize(save_path)
    logging.info("Image reduced from %s to %s [%s]", f"{input_size:n} B", 
        f"{result_size:n} B", 
        f"{(input_size - result_size) / input_size * 100:n}%")

    return input_size, result_size 


if __name__ == "__main__":
    app.run(main)
