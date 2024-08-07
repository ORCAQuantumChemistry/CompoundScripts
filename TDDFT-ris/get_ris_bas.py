import argparse



def gen_args():
    def str2bool(str):
        if str.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif str.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Unsupported value encountered.')
    parser = argparse.ArgumentParser(description='Davidson')
    parser.add_argument('-p',    '--pfunc',  type=str2bool,  default=False, help='extra p function each atom?')
    args = parser.parse_args()
    return args

args = gen_args()

input_filename = 'radi_exponent.txt'
output_filename = 'ris.bas' if not args.pfunc else 'ris+p.bas'

with open(input_filename, 'r') as file:
    lines = file.readlines()

# 处理文件内容并生成输出
with open(output_filename, 'w') as file:
    file.write('$DATA\n\n')

    for line in lines:
        if line.startswith('#'):
            continue  
        parts = line.split()

        element_symbol = parts[1].lower()
        theta_value = parts[-1]
        
        file.write(f'{element_symbol}\n')
        file.write('S   1\n')
        file.write(f'1         {theta_value}             1.0000000\n')
        if args.pfunc and element_symbol != 'h':
            file.write('P   1\n')
            file.write(f'1         {theta_value}             1.0000000\n')
            
        file.write('\n')

    file.write('$END')

print(f'Output written to {output_filename}')
