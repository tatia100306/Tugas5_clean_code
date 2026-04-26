MAX_GAJI = 1000
BPJS_RATE = 0.11

def hitung_gaji_bersih(gaji_pokok, tunjangan, pajak_persen):
    total = gaji_pokok + tunjangan
    total = total * pajak_persen / 100
    return min(total, MAX_GAJI)

def hitung_bpjs(gaji):
    return gaji * BPJS_RATE

def tampilkan_gaji(gaji, bpjs):
    print("Gaji bersih:", gaji)
    print("BPJS:", bpjs)