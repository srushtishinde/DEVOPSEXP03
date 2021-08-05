# python program
print('--------------------------------------')
print(f'**** PLAYFAIR CIPHER TEXT ****')
# plaintext
pt = input('Enter plaintext = ')
pt = pt.upper()

# key
k = input('Enter key = ')
k = k.upper()

# letters
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#creating matrix
matrix = []

for key in k.upper():
    if key not in matrix:
        matrix.append(key)
print('--------------------------------------')
print(f'Key = {matrix}')

for key in l:
    if key not in matrix:
        if (key == 'J'):
            x = 'hello'
        else:
            matrix.append(key)

# keyword 5x5 matrix
kmat = []

for key in range(5):
    kmat.append('')


def pos(kmat, lts):
	x = y = 0
	for i in range(5):
		for j in range(5):
			if kmat[i][j] == lts:
				x = i
				y = j

	return (x, y)

# strip matrix
kmat[0] = matrix[0:5]
kmat[1] = matrix[5:10]
kmat[2] = matrix[10:15]
kmat[3] = matrix[15:20]
kmat[4] = matrix[20:25]

# display matrix
print(f'Keyword matrix for Playfair cipher = ')
print(kmat[0])
print(kmat[1])
print(kmat[2])
print(kmat[3])
print(kmat[4])
print('--------------------------------------')
# check message
msg = []
for p in pt:
    msg.append(p)
for u in msg:
    if u == '':
        msg.remove('')

#even length
print(f'Entered plaintext = {msg}')
i = 0
lgt = int(len(msg)/2)

for both in range(lgt):
    if msg[i]== msg[i+1]:
        msg.insert(i+1,'X')
    i = i + 2

#odd length
if len(msg)%2 == 1:
    msg.append('X')
i = 0
nmsg = []
lgt1 = int(len(msg)/2)+1

for x in range(1,lgt1):
    nmsg.append(msg[i:i+2])
    i=i+2    
print(f'Pairing = {nmsg}\n')
print('--------**** FOR ENCRYPTION ****----------------')
q = 0
cipher = []
for key in nmsg:
    p1,q1 = pos(kmat, key[0])
    p2,q2 = pos(kmat, key[1])
    
    if (p1==p2):
        if q1 == 4:
            q1 = -1
        if q2 == 4:
            q2 = -1
        cipher.append(kmat[p1][q1+1])
        cipher.append(kmat[p1][q2+1])
    elif (q1==q2):
        if p1==4:
            p1 = -1
        if p2 == 4:
            p2 = -1
        cipher.append(kmat[p1+1][q1])
        cipher.append(kmat[p2+1][q2])
    else:
        cipher.append(kmat[p1][q2])
        cipher.append(kmat[p2][q1])
# display cipher text
print(str(f'Encryption = {cipher}'))

s1 = ''.join(cipher)
i = 0

ciphermat = []
for x in range(int(len(cipher)/2)):
    ciphermat.append(cipher[i:i+2])
    i=i+2
        
print(f'Cipher = {ciphermat}\n')

print('--------**** FOR DECRYPTION ****------------')
msg1 = []
for key in ciphermat:
    p1,q1 = pos(kmat, key[0])
    p2,q2 = pos(kmat, key[1])
    if p1==p2:
        if q1==4:
            q1=-1
        if q2==4:
            q2=-1
        msg1.append(kmat[p1][q1-1])
        msg1.append(kmat[p1][q2-1])
    elif q1==q2:
        if p1==4:
            p1=-1
        if p2==4:
            p2=-1
        msg1.append(kmat[p1-1][q1])
        msg1.append(kmat[p2-1][q2])
    else:
        msg1.append(kmat[p1][q2])
        msg1.append(kmat[p2][q1])

for u in range(len(msg1)):
    if 'X' in msg1:
        msg1.remove('X')

print(f'Ciphered Text = {ciphermat}\n')
print(f'Decryption (plaintext) = {str(msg1).strip()}')
