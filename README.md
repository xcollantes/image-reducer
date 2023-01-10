# Image reducer  

## Usage

1. Install dependencies.  

   ```shell
   python3 -m venv env  
   env/bin/pip install -r requirements.txt
   ```

1. Basic usage with an image named `cats.jpg` in a directory:

   ```shell  
   env/bin/python3 image_reducer.py --input some_dir/cats.jpg
   ```

   Other flags can be used:

   ```shell  
   env/bin/python3 image_reducer.py --input some_dir/cats.jpg 
   ```

   - `--input STRING` Directory or file to compress images.  If directory, the
   entire sub-directories tree will be recursively compressed.  

   - `--append_to_name STRING` String to add to new image filename after the
     original.

   - `--quality INTEGER` Level of quality for the output image.  Integer between
     100. By default is 40.  The higher the number, the lower the compression.
     The lower the number, the higher the compression and lower quality.

   - `--webp` Include flag to convert to web efficient WEBP format.
