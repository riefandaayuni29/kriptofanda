
abjad = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key = int(input('Masukkan cipher key yang anda inginkan (dalam angka, misal 9): '))  

def Caesar_cipher(kalimat,cipher_key): 
  kalimat = kalimat.upper()
  hasil_Caesar_cipher = '' 
  for karakter in kalimat: 
    if karakter in abjad:
      index_lama = abjad.index(karakter) 
      index_baru = (index_lama + cipher_key ) % len(abjad) 
      abjad_baru = abjad[index_baru] 
      hasil_Caesar_cipher = hasil_Caesar_cipher + abjad_baru 
    else:
       hasil_Caesar_cipher = hasil_Caesar_cipher + " " 
  return hasil_Caesar_cipher 

print("Masukkan pilihan")
print("1. Enkripsi")
print("2. Dekripsi")
pil = int(input()) 
if pil == 1:
  kalimat = input('Masukkan kalimat yang ingin dienkripsi : ') 
  kalimat_hasil = Caesar_cipher(kalimat,key) 
  print('Kalimat yang dimasukkan adalah:',kalimat)
  print('Hasil enkripsi kalimat menggunakan Caesar Cipher dengan key:',key, 'adalah', kalimat_hasil) 
  
elif pil == 2:
  kalimat_enkripsi = input('Masukkan kalimat yang ingin didekripsi : ') 
  kalimat_awal = Caesar_cipher(kalimat_enkripsi,-key) 
  print('Hasil Dekripsi Kalimat menggunakan Caesar chiper dengan key negatif adalah:',-key, 'adalah', kalimat_awal) 

else:
  print("Pilihan yang anda masukkan salah") 
