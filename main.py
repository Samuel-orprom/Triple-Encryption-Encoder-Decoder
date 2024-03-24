chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']


def encode(message, offset=13):
  enc_chars = str.maketrans(
      f'{chars[0]}{chars[1]}',
      f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}'
  )
  return str.translate(message, enc_chars)


def decode(message, offset=13):
  dec_chars = str.maketrans(
      f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}',
      f'{chars[0]}{chars[1]}')
  return str.translate(message, dec_chars)


get_option = input("Choose [e]ncode or [d]ecode (Default: e): ")
if get_option == 'e':
  message = input('Enter your plaintext message: ')
  offset = 16
  caesarshifted = {encode(message, offset)}

  letters = list(caesarshifted)

  aswitch = [sub.replace('a', '11') for sub in letters]
  Aswitch = [sub.replace('A', '11') for sub in aswitch]
  bswitch = [sub.replace('b', '12') for sub in Aswitch]
  Bswitch = [sub.replace('B', '12') for sub in bswitch]
  cswitch = [sub.replace('c', '13') for sub in Bswitch]
  Cswitch = [sub.replace('C', '13') for sub in cswitch]
  dswitch = [sub.replace('d', '14') for sub in Cswitch]
  Dswitch = [sub.replace('D', '14') for sub in dswitch]
  eswitch = [sub.replace('e', '15') for sub in Dswitch]
  Eswitch = [sub.replace('E', '15') for sub in eswitch]
  fswitch = [sub.replace('f', '21') for sub in Eswitch]
  Fswitch = [sub.replace('F', '21') for sub in fswitch]
  gswitch = [sub.replace('g', '22') for sub in Fswitch]
  Gswitch = [sub.replace('G', '22') for sub in gswitch]
  hswitch = [sub.replace('h', '23') for sub in Gswitch]
  Hswitch = [sub.replace('H', '23') for sub in hswitch]
  iswitch = [sub.replace('i', '24') for sub in Hswitch]
  Iswitch = [sub.replace('I', '24') for sub in iswitch]
  jswitch = [sub.replace('j', '25') for sub in Iswitch]
  Jswitch = [sub.replace('J', '25') for sub in jswitch]
  kswitch = [sub.replace('k', '13') for sub in Jswitch]
  Kswitch = [sub.replace('K', '13') for sub in kswitch]
  lswitch = [sub.replace('l', '31') for sub in Kswitch]
  Lswitch = [sub.replace('L', '31') for sub in lswitch]
  mswitch = [sub.replace('m', '32') for sub in Lswitch]
  Mswitch = [sub.replace('M', '32') for sub in mswitch]
  nswitch = [sub.replace('n', '33') for sub in Mswitch]
  Nswitch = [sub.replace('N', '33') for sub in nswitch]
  oswitch = [sub.replace('o', '34') for sub in Nswitch]
  Oswitch = [sub.replace('O', '34') for sub in oswitch]
  pswitch = [sub.replace('p', '35') for sub in Oswitch]
  Pswitch = [sub.replace('P', '35') for sub in pswitch]
  qswitch = [sub.replace('q', '41') for sub in Pswitch]
  Qswitch = [sub.replace('Q', '41') for sub in qswitch]
  rswitch = [sub.replace('r', '42') for sub in Qswitch]
  Rswitch = [sub.replace('R', '42') for sub in rswitch]
  sswitch = [sub.replace('s', '43') for sub in Rswitch]
  Sswitch = [sub.replace('S', '43') for sub in sswitch]
  tswitch = [sub.replace('t', '44') for sub in Sswitch]
  Tswitch = [sub.replace('T', '44') for sub in tswitch]
  uswitch = [sub.replace('u', '45') for sub in Tswitch]
  Uswitch = [sub.replace('U', '45') for sub in uswitch]
  vswitch = [sub.replace('v', '51') for sub in Uswitch]
  Vswitch = [sub.replace('V', '51') for sub in vswitch]
  wswitch = [sub.replace('w', '52') for sub in Vswitch]
  Wswitch = [sub.replace('W', '52') for sub in wswitch]
  xswitch = [sub.replace('x', '53') for sub in Wswitch]
  Xswitch = [sub.replace('X', '53') for sub in xswitch]
  yswitch = [sub.replace('y', '54') for sub in Xswitch]
  Yswitch = [sub.replace('Y', '54') for sub in yswitch]
  zswitch = [sub.replace('z', '55') for sub in Yswitch]
  Zswitch = [sub.replace('Z', '55') for sub in zswitch]

  oneswitch = [sub.replace('1', '.---- ') for sub in Zswitch]
  twoswitch = [sub.replace('2', '..--- ') for sub in oneswitch]
  threeswitch = [sub.replace('3', '...-- ') for sub in twoswitch]
  fourswitch = [sub.replace('4', '....- ') for sub in threeswitch]
  fiveswitch = [sub.replace('5', '..... ') for sub in fourswitch]
  sixswitch = [sub.replace('6', '-.... ') for sub in fiveswitch]
  sevenswitch = [sub.replace('7', '--... ') for sub in sixswitch]
  eightswitch = [sub.replace('8', '---.. ') for sub in sevenswitch]
  nineswitch = [sub.replace('9', '----. ') for sub in eightswitch]
  spaceswitch = [sub.replace(' ', '/') for sub in nineswitch]

  print(''.join(spaceswitch))

elif get_option == 'd':
  message = input('Enter your ciphertext message: ')
  offset = 16

  spaceswitch = [sub.replace('/', ' ') for sub in message]

  joinedspace = ''.join(spaceswitch)
  
  letters = joinedspace.split()
  print(letters)

  oneswitch = [sub.replace('.----', '1') for sub in letters]
  twoswitch = [sub.replace('..---', '2') for sub in oneswitch]
  threeswitch = [sub.replace('...--', '3') for sub in twoswitch]
  fourswitch = [sub.replace('....-', '4') for sub in threeswitch]
  fiveswitch = [sub.replace('.....', '5') for sub in fourswitch]
  sixswitch = [sub.replace('-....', '6') for sub in fiveswitch]
  sevenswitch = [sub.replace('--...', '7') for sub in sixswitch]
  eightswitch = [sub.replace('---..', '8') for sub in sevenswitch]
  nineswitch = [sub.replace('----.', '9') for sub in eightswitch]
  
  aswitch = [sub.replace('11', 'a') for sub in nineswitch]
  bswitch = [sub.replace('12', 'b') for sub in aswitch]
  cswitch = [sub.replace('13', 'c') for sub in bswitch]
  dswitch = [sub.replace('14', 'd') for sub in cswitch]
  eswitch = [sub.replace('15', 'e') for sub in dswitch]
  fswitch = [sub.replace('21', 'f') for sub in eswitch]
  gswitch = [sub.replace('22', 'g') for sub in fswitch]
  hswitch = [sub.replace('23', 'h') for sub in gswitch]
  iswitch = [sub.replace('24', 'i') for sub in hswitch]
  jswitch = [sub.replace('25', 'j') for sub in iswitch]
  kswitch = [sub.replace('13', 'k') for sub in jswitch]
  lswitch = [sub.replace('31', 'l') for sub in kswitch]
  mswitch = [sub.replace('32', 'm') for sub in lswitch]
  nswitch = [sub.replace('33', 'n') for sub in mswitch]
  oswitch = [sub.replace('34', 'o') for sub in nswitch]
  pswitch = [sub.replace('35', 'p') for sub in oswitch]
  qswitch = [sub.replace('41', 'q') for sub in pswitch]
  rswitch = [sub.replace('42', 'r') for sub in qswitch]
  sswitch = [sub.replace('43', 's') for sub in rswitch]
  tswitch = [sub.replace('44', 't') for sub in sswitch]
  uswitch = [sub.replace('45', 'u') for sub in tswitch]
  vswitch = [sub.replace('51', 'v') for sub in uswitch]
  wswitch = [sub.replace('52', 'w') for sub in vswitch]
  xswitch = [sub.replace('53', 'x') for sub in wswitch]
  yswitch = [sub.replace('54', 'y') for sub in xswitch]
  zswitch = [sub.replace('55', 'z') for sub in yswitch]
  
  joined = ''.join(zswitch)
  uncaesarshifted = {decode(joined, offset)}
  print(str(uncaesarshifted))

else:
  raise Exception(f'Invalid option: {get_option}')
