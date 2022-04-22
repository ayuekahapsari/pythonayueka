lama_pinjam = int(input("Pinjam buku berapa hari? "))

if lama_pinjam >= 3:
    print('Meminjam buku selama {} dikenakan biaya'.format (lama_pinjam))
else:
    print('Meminjam buku selama {} GRATIS'.format(lama_pinjam))
