## ==== IMPORT MODULES ====
import re
import binascii
import os
import math
from prettytable import PrettyTable


## ==== Functions ====

## splits the binary data into a list with delimiter ESC = b'\x1b'
def data_splitter(data):
    data_split = re.split(b'\x1b', data)
    if data_split[0] == b'':
        data_split = re.split(b'\x1b', data)
        if data_split[0] == b'':
            del data_split[0:1]
            for x in range(len(data_split)):
                data_split[x] = b'\x1b' + data_split[x]
        else:
            for x in range(len(data_split)):
                data_split[x] = b'\x1b' + data_split[x]
    else:
        for y in range(len(data_split)):
            if y == 0:
                data_split[y] = data_split[y]
            else:
                data_split[y] = b'\x1b' + data_split[y]
    return data_split


# end function


## load a prn file and splits it into a header, body and footer file
def split_prn(printername, filepath, outputfolder='prns'):
    """
    specify printername, original prn filepath and the desired outputfolder.
    Splits the prn file is three sections, header, body and footer, which can be loaded later on
    to create a custom prn file.
    File is saved as: <outputfolder>/<printername>-[section].prn
    """
    file = filepath
    map = outputfolder + '/' + printername

    ## load hex file
    with open(file, 'rb') as f:
        data = f.read()
    data_hex = binascii.hexlify(data)
    # end load


    data_split = data_splitter(data)
    for y in data_split:
        print(y)
    # print(data_split)

    endbody = []
    for i in range(len(data_split) - 1):
        if data_split[i][2:3] == b'\x47':
            startbody = i
        if data_split[i][2:3] == b'\x76':
            endbody.append(i)
        if data_split[i][-1:] == b'\x0c' and data_split[i + 1][1:2] == b'\x40':
            startfooter = i + 1
    #
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    ## get header file
    header = b''
    for x in range(0, startbody):
        header += data_split[x]
    # print(header)
    # end header
    ## write header file
    f = open(map + '-header.prn', 'wb')
    f.write(header)
    f.close()
    # end write header3

    ## get body till ESC i
    body = b''
    for x in range(startbody, endbody[0]):
        body += data_split[x]
    # print(body)
    # end body
    f = open(map + '-body.prn', 'wb')
    f.write(body)
    f.close()
    # end write body

    ## get footer
    footer = b''
    for x in range((len(data_split) - 3), len(data_split)):
        footer += data_split[x]
    # end footer
    f = open(map + '-footer.prn', 'wb')
    f.write(footer)
    f.close()


# end write footer
# endfunction



## print a hexadecimal byte in ascii
def print_hex(hbyte):
    if hbyte == b'\x00':
        return '00'
    else:
        return binascii.b2a_hex(hbyte.rstrip(b'\x00')).decode('utf-8')


# end


## convert ascii characters to their hex representative
def str_hex(letter):
    return letter.encode()


# end


## convert dec characters to their hex representative
def dec_hex(getal):
    return bytes([int(getal)])


# end


## convert hex to dec
def hex_dec(hexbyte):
    return ord(hexbyte)


# end

## convert 2 digit number to hex
def num_hex(input):
    bytearray.fromhex(str(input).zfill(2))


# end


## Save input as a file (write binary)
def save_prn_file(input, filename, folder=''):
    filename = filename+'.prn'
    if folder == '':
        path = filename
    else:
        path = folder + '/' + filename
        if not os.path.exists(folder):
            os.makedirs(folder)
    fx = open(path, 'wb')
    fx.write(input)
    fx.close()


# end


## load file (read binary)
def load_prn_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data


# end


## create an evenly spaced list with ones and zeros
def createnozzlelist(nozzles, activen, spacing, firstnozzle=1):
    list = [0] * nozzles
    for x in range(activen):
        list[x * (spacing + 1) + firstnozzle] = 1
    return list


# end


## create a nozzlelist, takes a list of active nozzles and converts this to ones and zeros on the specified places
def createnozzlelistsp(nozzles, nozzlelist, firstnozzle=0):
    list = [0] * nozzles
    for x in nozzlelist:
        list[x + firstnozzle] = 1
    return list


# end


## convert micrometers to inches
def um_in(input):
    return 1 / 25400 * input


# end


## convert inches to micrometers
def in_um(input):
    return input * 25400


# end


## Round to specified number of sigfigs
def rsf(num, sig_figs=5):
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0


# end




## view a prn file, in hexadecimal bytes. Values need to be converted to decimals for calculations.
## Only view, like perl script: parse-escp2
def body_viewer(filepath):
    ## load body file
    with open(filepath, 'rb') as f:
        data = f.read()
    # end load

    ## split data
    body_split = data_splitter(data)
    # done

    ## init table
    t = PrettyTable(['Command', 'hex format', 'Description'])
    t.align = "l"

    ## define strings for table
    c_escbG = ['ESC ( G ', '    (  G nL nH  m']
    c_escbU = ['ESC ( U ', '    (  U nL nH  P  V  H mL mH']
    c_escbK = ['ESC ( K ', '    (  K nL nH  m  n']
    c_escbi = ['ESC ( i ', '    (  i nL nH  n']
    c_escU = ['ESC U ', '    U  n']
    c_escbe = ['ESC ( e ', '    (  e nL nH  m  d']
    c_escbD = ['ESC ( D ', '    (  D nL nH rL rH  v  h']
    c_escbC = ['ESC ( C ', '    (  C nL nH m1 m2 m3 m4']
    c_escbc = ['ESC ( c ', '    (  c nL nH t1 t2 t3 t4 b1 b2 b3 b4']
    c_escbS = ['ESC ( S ', '    (  S nL nH w1 w2 w3 w4 l1 l2 l3 l4']
    c_escbm = ['ESC ( m ', '    (  m nL nH n']
    empty_row = ['', '', '']

    ## add/fill table rows
    for x in range(len(body_split)):
        if body_split[x][0:1] != b'\x1b':
            print('Error! body.prn in wrong format!')

        ## ESC ( G ...
        elif body_split[x][2:3] == b'G':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            m = body_split[x][5]

            # d_escbG = [c_escbG, seq,'Selecting graphics mode', c_escbG +' nL nH m']
            t.add_row([c_escbG[0], c_escbG[1], 'Selecting graphics mode'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( U ...
        elif body_split[x][2:3] == b'U':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            P = body_split[x][5]
            V = body_split[x][6]
            H = body_split[x][7]
            mL = body_split[x][8]
            mH = body_split[x][9]

            t.add_row([c_escbU[0], c_escbU[1], 'Set unit (expanded)'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( K ...
        elif body_split[x][2:3] == b'K':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            m = body_split[x][5]
            n = body_split[x][6]

            t.add_row([c_escbK[0], c_escbK[1], 'Monochrome/Color mode'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( i ...
        elif body_split[x][2:3] == b'i':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            n = body_split[x][5]

            t.add_row([c_escbi[0], c_escbi[1], 'MicroWeave mode'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC U ...
        elif body_split[x][1:2] == b'U':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            n = body_split[x][2]

            t.add_row([c_escU[0], c_escU[1], 'Unidirectional mode'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( e ...
        elif body_split[x][2:3] == b'e':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            m = body_split[x][5]
            d = body_split[x][6]

            t.add_row([c_escbe[0], c_escbe[1], 'Select dot size'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( D ...
        elif body_split[x][2:3] == b'D':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '
            nL = body_split[x][3]
            nH = body_split[x][4]
            rL = body_split[x][5]
            rH = body_split[x][6]
            v = body_split[x][7]
            h = body_split[x][8]

            t.add_row([c_escbD[0], c_escbD[1], 'Set raster resolution'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( C ...
        elif body_split[x][2:3] == b'C':
            nL = body_split[x][3]
            nH = body_split[x][4]
            m1 = body_split[x][5]
            m2 = body_split[x][6]
            m3 = body_split[x][7]
            m4 = body_split[x][8]

            t.add_row([c_escbC[0], c_escbC[1], 'Set page length'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( c ...
        elif body_split[x][2:3] == b'c':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            tL = body_split[x][5]
            tH = body_split[x][6]
            bL = body_split[x][7]
            bH = body_split[x][8]

            t.add_row([c_escbc[0], c_escbc[1], 'Set page format'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( S nl ....
        elif body_split[x][2:3] == b'S':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            w1 = body_split[x][5]
            w2 = body_split[x][6]
            w3 = body_split[x][7]
            w4 = body_split[x][8]
            l1 = body_split[x][9]
            l2 = body_split[x][10]
            l3 = body_split[x][11]
            l4 = body_split[x][12]

            t.add_row([c_escbS[0], c_escbS[1], 'Set paper dimensions'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        ## ESC ( m ...
        elif body_split[x][2:3] == b'm':
            seq = ''
            for y in range(len(body_split[x])):
                seq += print_hex(body_split[x][y:y + 1]) + ' '

            nL = body_split[x][3]
            nH = body_split[x][4]
            n = body_split[x][5]

            t.add_row([c_escbm[0], c_escbm[1], 'Set Print method ID'])
            t.add_row(['', seq, ''])
            t.add_row(empty_row)

        else:
            print('body.prn contains unknown ESC command')
    ## print table
    print(t)
    print('Done!')