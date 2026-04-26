def hitung_gaji(gaji_pokok, tunjangan, pajak_persen):
    gaji_pokok = gaji_pokok + tunjangan
    gaji_pokok = gaji_pokok * pajak_persen/100
    if gaji_pokok > 1000:
        gaji_pokok = 1000

    potongan_bpjs = gaji_pokok * 0.11
    print("Gaji bersih:", gaji_pokok)
    print("BPJS:", potongan_bpjs)
    return gaji_pokok, potongan_bpjs