def convert_img(image):
    ranges = [
        [0, 16, '██'],
        [16, 32, '▓▓'],
        [32, 48, '▒▒'],
        [48, 64, '░░'],
        [64, 80, '++'],
        [80, 96, '**'],
        [96, 112, '##'],
        [112, 128, '%%'],
        [128, 144, '&&'],
        [144, 160, '$$'],
        [160, 176, '##'],
        [176, 192, '@@'],
        [192, 208, '88'],
        [208, 224, '%%'],
        [224, 240, '^^'],
        [240, 256, '  ']
    ]
    
    range_dict = {
        '██': list(range(ranges[0][0], ranges[0][1])),
        '▓▓': list(range(ranges[1][0], ranges[1][1])),
        '▒▒': list(range(ranges[2][0], ranges[2][1])),
        '░░': list(range(ranges[3][0], ranges[3][1])),
        '++': list(range(ranges[4][0], ranges[4][1])),
        '**': list(range(ranges[5][0], ranges[5][1])),
        '##': list(range(ranges[6][0], ranges[6][1])),
        '%%': list(range(ranges[7][0], ranges[7][1])),
        '&&': list(range(ranges[8][0], ranges[8][1])),
        '$$': list(range(ranges[9][0], ranges[9][1])),
        '##': list(range(ranges[10][0], ranges[10][1])),
        '@@': list(range(ranges[11][0], ranges[11][1])),
        '88': list(range(ranges[12][0], ranges[12][1])),
        '%%': list(range(ranges[13][0], ranges[13][1])),
        '^^': list(range(ranges[14][0], ranges[14][1])),
        '  ': list(range(ranges[15][0], ranges[15][1]))
    }
    
    ascii_code = ''
    for row in image:
        for cell_value in row:
            if cell_value in range_dict['██']:
                character = '██'
            elif cell_value in range_dict['▓▓']:
                character = '▓▓'
            elif cell_value in range_dict['▒▒']:
                character = '▒▒'
            elif cell_value in range_dict['░░']:
                character = '░░'
            elif cell_value in range_dict['++']:
                character = '++'
            elif cell_value in range_dict['**']:
                character = '**'
            elif cell_value in range_dict['##']:
                character = '##'
            elif cell_value in range_dict['%%']:
                character = '%%'
            elif cell_value in range_dict['&&']:
                character = '&&'
            elif cell_value in range_dict['$$']:
                character = '$$'
            elif cell_value in range_dict['@@']:
                character = '@@'
            elif cell_value in range_dict['88']:
                character = '88'
            elif cell_value in range_dict['%%']:
                character = '%%'
            elif cell_value in range_dict['^^']:
                character = '^^'
            else:
                character = '  '
            ascii_code += character
        ascii_code += '\n'
    
    return ascii_code
def convert_img(image):
    ranges = [
        [0, 16, '██'],
        [16, 32, '▓▓'],
        [32, 48, '▒▒'],
        [48, 64, '░░'],
        [64, 80, '++'],
        [80, 96, '**'],
        [96, 112, '##'],
        [112, 128, '%%'],
        [128, 144, '&&'],
        [144, 160, '$$'],
        [160, 176, '##'],
        [176, 192, '@@'],
        [192, 208, '88'],
        [208, 224, '%%'],
        [224, 240, '^^'],
        [240, 256, '  ']
    ]
    
    range_dict = {
        '██': list(range(ranges[0][0], ranges[0][1])),
        '▓▓': list(range(ranges[1][0], ranges[1][1])),
        '▒▒': list(range(ranges[2][0], ranges[2][1])),
        '░░': list(range(ranges[3][0], ranges[3][1])),
        '++': list(range(ranges[4][0], ranges[4][1])),
        '**': list(range(ranges[5][0], ranges[5][1])),
        '##': list(range(ranges[6][0], ranges[6][1])),
        '%%': list(range(ranges[7][0], ranges[7][1])),
        '&&': list(range(ranges[8][0], ranges[8][1])),
        '$$': list(range(ranges[9][0], ranges[9][1])),
        '##': list(range(ranges[10][0], ranges[10][1])),
        '@@': list(range(ranges[11][0], ranges[11][1])),
        '88': list(range(ranges[12][0], ranges[12][1])),
        '%%': list(range(ranges[13][0], ranges[13][1])),
        '^^': list(range(ranges[14][0], ranges[14][1])),
        '  ': list(range(ranges[15][0], ranges[15][1]))
    }
    
    ascii_code = ''
    for row in image:
        for cell_value in row:
            if cell_value in range_dict['██']:
                character = '██'
            elif cell_value in range_dict['▓▓']:
                character = '▓▓'
            elif cell_value in range_dict['▒▒']:
                character = '▒▒'
            elif cell_value in range_dict['░░']:
                character = '░░'
            elif cell_value in range_dict['++']:
                character = '++'
            elif cell_value in range_dict['**']:
                character = '**'
            elif cell_value in range_dict['##']:
                character = '##'
            elif cell_value in range_dict['%%']:
                character = '%%'
            elif cell_value in range_dict['&&']:
                character = '&&'
            elif cell_value in range_dict['$$']:
                character = '$$'
            elif cell_value in range_dict['@@']:
                character = '@@'
            elif cell_value in range_dict['88']:
                character = '88'
            elif cell_value in range_dict['%%']:
                character = '%%'
            elif cell_value in range_dict['^^']:
                character = '^^'
            else:
                character = '  '
            ascii_code += character
        ascii_code += '\n'
    
    return ascii_code
