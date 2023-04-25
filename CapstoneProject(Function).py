#penjualan barang toko serbaguna
#alat tulis
#sembako
#peralatan mandi
#create, read, update, delete


from prettytable import PrettyTable
Daftar_barang = {
    'alat tulis': [
        {'Nama Barang': 'Pensil', 'Stock': 20, 'Harga': 5000, 'Merek': 'Faber-castell'},
        {'Nama Barang': 'Bolpen', 'Stock': 25, 'Harga': 10000, 'Merek': 'Snowman'}
    ],
    'peralatan mandi': [
        {'Nama Barang': 'Sabun mandi', 'Stock': 15, 'Harga': 35000, 'Merek': 'lifebuoy'},
        {'Nama Barang': 'Shampoo', 'Stock': 20, 'Harga': 25000, 'Merek': 'Head & shoulders'}
    ]
}
    

def Exit():
    print('')
    print('Terimakasih telah berkunjung di toko Serbaguna!')

def message(angka):
    if angka == 1:
        print('')
        print('Input tidak valid, silahkan coba lagi!')
    elif angka == 2:
        print('')
        print("Jenis barang tidak tersedia dalam daftar penjualan, silahkan coba lagi!")
    elif angka == 3:
        print('')
        print('barang tidak ditemukan, silahkan coba lagi!')
    elif angka == 4:
        print('')
    elif angka == 5:
        print('')
        print('data telah tersimpan')
    elif angka == 6:
        print('')
        print('data tidak tersimpan')   
    elif angka == 7:
        print('')
        print('data berhasil dihapus')
    elif angka == 8:
        print('')
        print('data tidak dihapus')
    elif angka == 9:
        print('')
        print('data berhasil diubah')
    elif angka == 10:
        print('')
        print('Terimakasih sudah belanja di toko Serbaguna!')
    elif angka == 11:
        print('Tolong hanya masukkan index yang ada dalam tabel')

    

def keseluruhan_table():
    print('')
    print('Berikut ini daftar seluruh penjualan di Toko Serbaguna: ')
    print('')
    for jenis_barang, item_barang in Daftar_barang.items():
        print(f'Jenis Barang: {jenis_barang}')
        table = PrettyTable(['Nama Barang', 'Stock', 'Harga', 'Merek'])
        for barang in item_barang:
            table.add_row([barang['Nama Barang'], barang['Stock'], barang['Harga'], barang['Merek']])
        print(table)
        print('')

def tampilkan_tabel_tertentu(barang):
    table = PrettyTable(['Nama Barang', 'Stock', 'Harga', 'Merek'])
    for item in Daftar_barang[barang]:
        table.add_row([item['Nama Barang'], item['Stock'], item['Harga'], item['Merek']])
    print(table)

def table_sesuai_keinginan():
    while True:
        print('')
        barangmana = input('Jenis barang apa yang anda mau lihat (alat tulis / peralatan mandi): ').lower()
        print('')
        if barangmana == 'alat tulis':
            print(f'jenis barang: {barangmana}')
            tampilkan_tabel_tertentu(barangmana)
            break
        elif barangmana == 'peralatan mandi':
            print(f'jenis barang: {barangmana}')
            tampilkan_tabel_tertentu(barangmana)
            break
        else:
            message(2)
            print('')

    
while True:
    Menu = input('''
        Selamat Datang di Toko Serbaguna!

        1. Daftar barang yang ada di Toko Serbaguna
        2. Menambahkan barang di Toko Serbaguna
        3. Mengubah barang di Toko Serbaguna
        4. Menghapus barang di Toko Serbaguna
        5. Exit
        
        Silahkan pilih Menu [1-5]: ''')
     

    if Menu =='1':
        while True:
            Menu1 = input('''
            1. Tampilkan seluruh barang yang tersedia
            2. Tampilkan barang dengan jenis barang tertentu (alat tulis / peralatan mandi)
            3. Kembali ke menu utama
            Silahkan pilih sub menu bagian tampilkan daftar penjualan [1-3]: ''')

            if Menu1 =='1': 
                keseluruhan_table()
                continue

            elif Menu1=='2':
                table_sesuai_keinginan()
                continue

            elif Menu1 =='3':
                break
            else:
                message(1)
                print('')
                continue
            

    elif Menu =='2':
        while True: 
            Menu2 = input('''
            1. Tambah data ke dalam daftar penjualan
            2. Kembali ke menu utama
            Silahkan pilih sub menu bagian tampilkan daftar penjualan [1-2]: '''
                        )

            if Menu2 =='1':
                while True:
                    print('')
                    barangapa = input('jenis barang apa yang mau di input (alat tulis / peralatan mandi): ').lower()
                    if barangapa in ['alat tulis', 'peralatan mandi']:
                        print('')
                        nama_barang = input('nama barang apa yang mau dimasukkan: ')
                        while True:
                            try:
                                stock = int(input('stock yang mau di input: '))
                                break
                            except:
                                message(1)
                                print('')
                        while True:
                            try:
                                harga = int(input('harganya berapa: '))
                                break
                            except:
                                message(1)
                                print('')
                        merek = input('merek apa nih: ')
                        new_item = {'Nama Barang': nama_barang.capitalize(), 'Stock': stock, 'Harga': harga, 'Merek': merek}
                        break
                    else:
                        message(2)
                        print('')
                        continue
                        
                while True:
                    print('')
                    simpan = input('apakah data mau disimpan (YA/TIDAK): ').upper()
                    if simpan == 'YA':
                        Daftar_barang[barangapa].append(new_item)
                        message(5)
                        break
        
                    elif simpan == 'TIDAK':
                        message(6)
                        break

                    else:
                        message(1)
                        print('')
    
            elif Menu2 == '2':  
                break
            else:
                message(1)
                print('')
                continue


    elif Menu =='3':
        while True:
            Menu3 = input('''
            1. Ubah data ke dalam penjualan
            2. Kembali ke menu utama
            Silahkan pilih sub menu bagian tampilkan daftar penjualan [1-2]: ''')

            if Menu3 == '1':
                while True:
                    print('')
                    ubahapa = input('jenis barang apa yang mau diubah (alat tulis / peralatan mandi): ').lower()
                    if ubahapa in ['alat tulis', 'peralatan mandi']:
                        print('')
                        print(f"Jenis barang: {ubahapa}")
                        tampilkan_tabel_tertentu(ubahapa)
                        while True:
                            namabarangtidakketemu = False
                            while not namabarangtidakketemu:
                                print('')
                                barangapaan = input('barang apa yang mau diubah: ')
                                for item in Daftar_barang[ubahapa]:
                                    if item['Nama Barang'].lower() == barangapaan.lower():
                                        namabarangtidakketemu = True
                                        
                                        while True:
                                            try:
                                                item['Stock'] = int(input('stocknya mau berapa: '))
                                                break
                                            except:
                                                message(1)
                                                print('')
                                        
                                        while True:
                                            try:
                                                item['Harga'] = int(input('harga mau berapa: '))
                                                break
                                            except:
                                                message(1)
                                                print('')
                                        item['Merek'] = input('merek mau apa: ')
                                        message(9)
                                        break
                                if not namabarangtidakketemu:
                                    message(3)
                                    print('')
                            break
                        break
                    
                    else:
                        message(2)
                        print('')
            
            elif Menu3 == '2':
                break
            else:
                message(1)
                print('')
                continue



    elif Menu == '4':
        while True:
            Menu4 = input('''
            1. hapus data di dalam penjualan
            2. Kembali ke menu utama
            Silahkan pilih sub menu bagian tampilkan daftar penjualan [1-2]: ''')

            if Menu4 =='1':
                while True:
                    print('')
                    hapusapa = input('jenis barang apa yang mau diubah (alat tulis / peralatan mandi): ').lower()
                    if hapusapa in ['alat tulis', 'peralatan mandi']:
                        print('')
                        print(f'jenis barang: {hapusapa}')
                        tampilkan_tabel_tertentu(hapusapa)

                        while True: #untuk ngecek apakah yang dimasukkan integer
                            try:
                                indexberapa = int(input('masukkan nomor index yang mau dihapus yang dimulai dari angka 0, dihitung dari atas: '))
                                break
                            except:
                                message(1)
                                print('')

                        while True: #untuk ngecek apakah int yang diinput ada didalam nomor indeks
                                indexberapa = int(input('masukkan nomor index yang mau dihapus yang dimulai dari angka 0, dihitung dari atas: '))
                                if indexberapa not in range(len(Daftar_barang['alat tulis'])):
                                    message(11)
                                else:
                                    break
                        while True:
                            yakin = input('apakah anda yakin mau hapus (YA/TIDAK): ').upper()
                            if yakin == 'YA':
                                del Daftar_barang['alat tulis'][indexberapa]
                                message(7)
                                break
                            elif yakin == 'TIDAK':
                                message(8)       
                                break
                        break
                    else:
                        message(1)
                        print('')
                        continue
    
            elif Menu4 == '2':
                break
            else:
                message(1)
                print('')
                continue

    elif Menu =='5':
        message(10)
        print('')
        break
    
    else:
        message(1)





