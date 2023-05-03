#penjualan barang toko serbaguna
#alat tulis
#sembako
#peralatan mandi
#create, read, update, delete


from prettytable import PrettyTable
Daftar_barang = {
    'alat tulis': [
        {'Nama Barang': 'Pensil', 'Stock': 20, 'Harga': 5000, 'Merek': 'Faber-castell', 'Rak Penyimpanan' : 'Rak A'},
        {'Nama Barang': 'Bolpen', 'Stock': 25, 'Harga': 10000, 'Merek': 'Snowman', 'Rak Penyimpanan' : 'Rak B'}
    ],
    'peralatan mandi': [
        {'Nama Barang': 'Sabun mandi', 'Stock': 15, 'Harga': 35000, 'Merek': 'lifebuoy', 'Rak Penyimpanan' : 'Rak C'},
        {'Nama Barang': 'Shampoo', 'Stock': 20, 'Harga': 25000, 'Merek': 'Head & shoulders', 'Rak Penyimpanan' : 'Rak D'}
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
    elif angka == 12:
        print('Stock tidak cukup, silahkan pilih menu ulang ')

    
def keseluruhan_table():
    print('')
    print('Berikut ini daftar seluruh penjualan di Toko Serbaguna: ')
    print('')
    for jenis_barang, item_barang in Daftar_barang.items():
        print(f'Jenis Barang: {jenis_barang}')
        sorted_items = sorted(item_barang, key=lambda x: x['Stock'])
        table = PrettyTable(['Nama Barang', 'Stock', 'Harga', 'Merek', 'Rak Penyimpanan'])
        for barang in sorted_items:
            table.add_row([barang['Nama Barang'], barang['Stock'], barang['Harga'], barang['Merek'], barang['Rak Penyimpanan']])
        print(table)
        print('')


def tampilkan_tabel_tertentu(barang):
    items = Daftar_barang[barang]
    sorted_items = sorted(items, key=lambda x: x['Stock'])
    table = PrettyTable(['Nama Barang', 'Stock', 'Harga', 'Merek', 'Rak Penyimpanan'])
    for item in sorted_items:
        table.add_row([item['Nama Barang'], item['Stock'], item['Harga'], item['Merek'], item['Rak Penyimpanan']])
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
                        RakPenyimpanan = input('masukkan Rak Penyimpanan: ')
                        new_item = {'Nama Barang': nama_barang.capitalize(), 'Stock': stock, 'Harga': harga, 'Merek': merek, 'Rak Penyimpanan': RakPenyimpanan}
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
            2. Memasukkan stock barang ke dalam penjualan
            3. Mengeluarkan stock barang ke dalam penjualan
            4. Kembali ke menu utama
            Silahkan pilih sub menu bagian tampilkan daftar penjualan [1-4]: ''')

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
                                        item['Rak Penyimpanan']= input('masukkan Rak Penyimpanan: ')
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
                while True:
                    print('')
                    masukkanapa = input('jenis barang apa yang mau masukkan (alat tulis / peralatan mandi): ').lower()
                    if masukkanapa in ['alat tulis', 'peralatan mandi']:
                        print('')
                        print(f'jenis barang: {masukkanapa}')
                        tampilkan_tabel_tertentu(masukkanapa)
                        while True:
                            barangapayangmaudimasukkan = input('barang apa yang mau dimasukkan: ')
                            item_found = False
                            for item in Daftar_barang[masukkanapa]:
                                if item['Nama Barang'].lower() == barangapayangmaudimasukkan.lower():
                                    item_found = True
                                    while True:
                                        try:
                                            stocktambahan = int(input('mau dimasukkan berapa: '))
                                            break
                                        except:
                                            message(1)
                                            print('')

                                    stockbarubarang = item['Stock'] + stocktambahan
                                    while True:
                                        yakinmaumasukkan = input('apakah anda yakin mau masukkan barang tersebut (YA/TIDAK): ').upper()
                                        if yakinmaumasukkan == 'YA':
                                            item['Stock'] = stockbarubarang
                                            message(5)
                                            break
                                        elif yakinmaumasukkan == 'TIDAK':
                                            message(6)
                                            break
                                        else:
                                            message(1)
                                        
                            if not item_found:
                                message(3)
                                print('')
                            else:
                                break
                        break
                    else:
                        message(2)
                        print('')


            
            elif Menu3 == '3':
                while True:
                    print('')
                    mengeluarkanapa = input('jenis barang apa yang mau dikeluarkan (alat tulis / peralatan mandi): ').lower()
                    if mengeluarkanapa in ['alat tulis', 'peralatan mandi']:
                        print('')
                        print(f'jenis barang: {mengeluarkanapa}')
                        tampilkan_tabel_tertentu(mengeluarkanapa)
                        item_found = False
                        while not item_found:
                            barangkeluar = input('barang apa yang mau keluarkan: ')
                            for item in Daftar_barang[mengeluarkanapa]:
                                if item['Nama Barang'].lower() == barangkeluar.lower():
                                    item_found = True
                                    while True:
                                        try:
                                            totalbarangkeluar = int(input('mau dikeluarkan berapa: '))
                                            break
                                        except:
                                            message(1)
                                            print('')
                                    
                                    if totalbarangkeluar <= item['Stock']:
                                        stockbaru = item['Stock'] - totalbarangkeluar
                                        print('')
                                        while True:
                                            yakinmaukeluarkan = input('apakah anda yakin mau keluarkan barang tersebut (YA/TIDAK): ').upper()
                                            if yakinmaukeluarkan == 'YA':
                                                item['Stock'] = stockbaru
                                                message(5)
                                                break
                                            elif yakinmaukeluarkan == 'TIDAK':
                                                message(6)
                                                break
                                            else:
                                                message(1)
                                        break
                                    else:
                                        message(12)
                                        break
                            if not item_found:
                                message(3)
                                print('')
                        if item_found:
                            break
                    else:
                        message(2)
                        print('')
    

            elif Menu3 == '4':
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


                        if indexberapa in range(len(Daftar_barang[hapusapa])):
                            sorted_items = sorted(Daftar_barang[hapusapa], key=lambda x: x['Stock'])
                            item_to_remove = sorted_items[indexberapa]
                            index_to_remove = Daftar_barang[hapusapa].index(item_to_remove)
                       
                            while True:
                                yakin = input('apakah anda yakin mau hapus (YA/TIDAK): ').upper()
                                if yakin == 'YA':
                                    del Daftar_barang[hapusapa][index_to_remove]
                                    message(7)
                                    break
                                elif yakin == 'TIDAK':
                                    message(8)       
                                    break
                                else: 
                                    message(1)
                                    print('')
                            break
                        else:
                            message(11)
                            print('')
                    else:
                        message(2)
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



