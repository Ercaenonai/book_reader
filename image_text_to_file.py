from output_text_files import ExtractTextFromImage as Et

# set image source input folder
image_folder = 'where_the_wild_things_are'

# set text output folder
output_folder = 'text_out_test_ud'

# options for image processing enhancement.
proc_list = [
             # 'BLUR',
             # 'CONTOUR',
             # 'DETAIL',
             # 'EDGE_ENHANCE',
             # 'EDGE_ENHANCE_MORE',
             # 'EMBOSS',
             # 'FIND_EDGES',
             # 'SMOOTH',
             # 'SMOOTH_MORE',
             'SHARPEN'
             ]

# choose whether to see images, print output, and hear text output per image proc. y or n.
show_image = 'n'

print_output = 'y'

hear_output = 'y'

# instantiates class with output folder and image folder.
funcs = Et(output_folder=output_folder,
           image_folder=image_folder)


def main():
    funcs.create_output_folder()

    # runs extract text function with vars assigned above.
    funcs.extract_text(proc_list=proc_list,
                       show_image=show_image,
                       print_output=print_output,
                       hear_output=hear_output)


if __name__ == '__main__':
    main()
