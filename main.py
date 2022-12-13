from rembg import remove
from PIL import Image
from pathlib import Path


def remove_bg():
    list_of_exetetions = ['*.png'] #, '*.jpg', '*.jpeg']
    all_files = []

    for ext in list_of_exetetions:
        all_files.extend(Path('.\input_imgs').glob(ext))

    #print(all_files)
    for item in all_files:
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'{file_name}_output.png'
        print(output_path)


def main():
    remove_bg()


if __name__ == '__main__':
    main()
