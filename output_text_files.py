import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import glob
import os
import pyttsx3


class ExtractTextFromImage:
    # windows install location. see readme for link for other OS and install instructions.
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    root_path = os.path.dirname(os.path.abspath("__file__"))

    # initializes pyttsx engine to "speak" audio and sets speed
    engine = pyttsx3.init()

    voice_rate = 145

    def __init__(self,
                 root_path: str = root_path,
                 image_folder: str = None,
                 output_folder: str = None):
        self.root_path = root_path
        self.image_folder = image_folder
        self.output_folder = output_folder
        self.engine.setProperty('rate', self.voice_rate)
        self.img_lst = []

    # function for checking/creating output folder. allows user to cancel if exists.
    def create_output_folder(self):
        if not os.path.exists(os.path.join(self.root_path, self.output_folder)):
            os.mkdir(os.path.join(self.root_path, self.output_folder))

        else:
            response = input('WARNING: Output folder already exists. If you continue, '
                             'all contents will be replaced. y/n: ')

            response = response.lower()

            while response not in ('y', 'n'):
                print('Incorrect value entered')

                response = input('please enter y or n: ')

            if response != 'y':
                print('Enter a new output folder and run again')

                exit()

    # function for opening and sorting input images to extract text. assumes images are saved with numeric ordering.
    # todo ensure images are png or alter to allow jpg. maybe adjust for non numeric.
    def open_images_sort(self):
        for name in glob.glob(os.path.join(self.root_path, self.image_folder) + "/*.png"):
            self.img_lst.append(name)

        # sorts the list by numeric order to check output against input
        self.img_lst.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

        return self.img_lst

    # allows for different image processing depending on source image
    # todo would like to make this a bit cleaner without all the if statements.
    @staticmethod
    def preprocess_image(image, proc_list):
        for f in proc_list:
            if f == 'BLUR':
                image = image.filter(ImageFilter.SHARPEN)

            elif f == 'CONTOUR':
                image = image.filter(ImageFilter.CONTOUR)

            elif f == 'DETAIL':
                image = image.filter(ImageFilter.DETAIL)

            elif f == 'EDGE_ENHANCE':
                image = image.filter(ImageFilter.DETAIL)

            elif f == 'EDGE_ENHANCE_MORE':
                image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

            elif f == 'EMBOSS':
                image = image.filter(ImageFilter.EMBOSS)

            elif f == 'FIND_EDGES':
                image = image.filter(ImageFilter.FIND_EDGES)

            elif f == 'SMOOTH':
                image = image.filter(ImageFilter.SMOOTH)

            elif f == 'SMOOTH_MORE':
                image = image.filter(ImageFilter.SMOOTH_MORE)

            elif f == 'SHARPEN':
                image = image.filter(ImageFilter.SHARPEN)

            else:
                pass

        return image

    # accepts user defined arguments in main script and processes all images to text files
    def extract_text(self, proc_list, show_image, print_output, hear_output):
        count = 0

        img_lst = self.open_images_sort()

        for i in img_lst:
            image = Image.open(i).convert('RGB')

            image = self.preprocess_image(image, proc_list)

            enhancer = ImageEnhance.Brightness(image)

            factor = 1.75

            image = enhancer.enhance(factor)

            text = pytesseract.image_to_string(image, lang='eng', nice=10)

            show_image = str(show_image).lower()

            print_output = str(print_output).lower()

            hear_output = str(hear_output).lower()

            if show_image == 'y':
                image.show()

            else:
                pass

            if print_output == 'y':
                print(text)

            else:
                pass

            if hear_output == 'y':
                self.engine.say(text)

                self.engine.runAndWait()

            else:
                pass

            if not text:
                print('page appears blank')

            response = input('Does the output text match the image text? y/n: ')

            response = str(response).lower()

            while response not in ('y', 'n'):
                print('please enter valid response y/n: ')

                response = input('valid response y or n: ')

                response = str(response).lower()

            if response != 'y':
                print('please enter text correctly: ')

                # overwrites text var with user input
                text = str(input())

            if text != '':
                count += 1

                page = ''.join(['page_', str(count)])

                with open(os.path.join(self.root_path, self.output_folder) + f"/{page}.txt", "w") as text_file:
                    text_file.write(text)

            else:
                pass


class InputText(ExtractTextFromImage):
    # function for manual text input and file write.
    def input_text(self):
        count = 0

        text = ''

        while text != 'quit':
            text = input('Enter line of text. type quit to finish: ')

            if text != 'quit':
                count += 1

                print(text, count)

                with open(os.path.join(self.root_path, self.output_folder) + f"/{count}.txt", "w") as text_file:
                    text_file.write(text)
