



def convert_img(image):
    ranges = [[0, 64, '█'], [64, 128, 'O'], [128, 192, 'I'], [192, 256, '.']]
    range_dict = {
        '█': list(range(ranges[0][0], ranges[0][1])),
        'O': list(range(ranges[1][0], ranges[1][1])),
        'I': list(range(ranges[2][0], ranges[2][1])),
        '.': list(range(ranges[3][0], ranges[3][1]))
    }
    ascii_code = ''
    for row in image:
        for cell_value in row:
            if cell_value in range_dict['█']:
                character = '█'
            elif cell_value in range_dict['O']:
                character = 'O'
            elif cell_value in range_dict['I']:
                character = 'I'
            else:
                character = '.'
            ascii_code = ascii_code + character
        ascii_code = ascii_code + '\n'
    return ascii_code
            

