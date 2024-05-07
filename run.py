import argparse
import img_reader




def runner(args):
    # Read the source image and return the grayscale matrix with values between 0-255
    image = img_reader.read_img(args.source_path)
    # Convert grayscale matrix to ASCII characters
    ascii = 



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_path', help='path to source image', required=True)
    parser.add_argument('--target_path', help='path to target file')
    args = parser.parse_args()

    runner(args)
