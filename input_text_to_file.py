from output_text_files import InputText as It

# set text output folder
output_folder = 'text_input_test_out'

funcs = It(output_folder=output_folder)


def main():
    funcs.create_output_folder()

    funcs.input_text()


if __name__ == '__main__':
    main()
