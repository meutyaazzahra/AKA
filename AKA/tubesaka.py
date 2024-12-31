# Program Optimasi Pengiriman Paket dengan Drone dalam E-Commerce

# Fungsi untuk menghitung biaya pengiriman berdasarkan jarak
def hitung_biaya(jarak_km, biaya_per_10km):
    return (jarak_km / 10) * biaya_per_10km

# Fungsi untuk menampilkan informasi drone
def tampilkan_informasi_drone(kapasitas_berat, baterai, kecepatan, daya_jelajah):
    print("=" * 40)
    print(f"Kapasitas berat maksimum drone: {kapasitas_berat} kg")
    print(f"Sisa baterai drone: {baterai}%")
    print(f"Kecepatan maksimum drone: {kecepatan} km/jam")
    print(f"Daya jelajah drone per pengisian: {daya_jelajah} km")
    print("=" * 40)

# Fungsi untuk menampilkan rute pengiriman
def tampilkan_rute(rute):
    print("=" * 40)
    print("Rute pengiriman:")
    for i, lokasi in enumerate(rute, start=1):
        print(f"{i}. {lokasi}")
    print("=" * 40)

# Input data awal
biaya_per_10km = 5000  # biaya pengiriman per 10 km dalam Rupiah

# Data drone berdasarkan jenis pengiriman
drone_short_hop = {
    "kapasitas_berat": 5,
    "baterai_awal": 100,
    "jarak_tempuh_maks": 7,
    "kecepatan": 54
}

drone_high_speed = {
    "kapasitas_berat": 10,
    "baterai_awal": 100,
    "jarak_tempuh_maks": 100,
    "kecepatan": 100
}

# Memilih jenis pengiriman
print("Pilih jenis pengiriman:")
print("1. Short-hop (pengiriman jarak pendek)")
print("2. High-speed & Long-distance (pengiriman cepat jarak jauh)")
pilihan = int(input("Masukkan pilihan (1/2): "))

if pilihan == 1:
    drone = drone_short_hop
    jenis_pengiriman = "Short-hop"
elif pilihan == 2:
    drone = drone_high_speed
    jenis_pengiriman = "High-speed & Long-distance"
else:
    print("Pilihan tidak valid!")
    exit()

# Input data dari kurir
print("Masukkan data pengiriman:")
rute_pengiriman = []
jarak_setiap_tujuan = []
berat_barang = []

jumlah_lokasi = int(input("Masukkan jumlah lokasi pengiriman: "))
for i in range(jumlah_lokasi):
    lokasi = input(f"Masukkan nama lokasi ke-{i + 1}: ")
    rute_pengiriman.append(lokasi)
    jarak = float(input(f"Masukkan jarak ke {lokasi} (km): "))
    jarak_setiap_tujuan.append(jarak)
    berat = float(input(f"Masukkan berat barang untuk {lokasi} (kg): "))
    berat_barang.append(berat)

# Validasi berat barang
if sum(berat_barang) > drone["kapasitas_berat"]:
    print("=" * 40)
    print("Error: Berat barang melebihi kapasitas drone!")
    print("=" * 40)
else:
    # Hitung total jarak dan biaya pengiriman
    total_jarak = sum(jarak_setiap_tujuan)
    total_biaya = hitung_biaya(total_jarak, biaya_per_10km)

    # Periksa apakah jarak melebihi kemampuan drone
    if total_jarak > drone["jarak_tempuh_maks"]:
        print("=" * 40)
        print("Error: Jarak pengiriman melebihi jarak tempuh maksimum drone!")
        print("=" * 40)
    else:
        # Tampilkan informasi pengiriman
        tampilkan_rute(rute_pengiriman)
        print(f"Jenis pengiriman: {jenis_pengiriman}")
        print(f"Total jarak pengiriman: {total_jarak} km")
        print(f"Total biaya pengiriman: Rp{total_biaya}")
        print("=" * 40)
        print("Berat barang ke setiap lokasi:")
        for i in range(len(berat_barang)):
            print(f"Lokasi {rute_pengiriman[i]}: {berat_barang[i]} kg")
        print("=" * 40)

        # Tampilkan informasi drone
        tampilkan_informasi_drone(drone["kapasitas_berat"], drone["baterai_awal"], drone["kecepatan"], drone["jarak_tempuh_maks"])
