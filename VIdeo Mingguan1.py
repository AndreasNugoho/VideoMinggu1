#Andreas Nugroho
#71200646

#david meminjam uang dibank sebesar Rp.200.000.000 dengan angsuran 6.000.000 per bulan selama 47 kali. 
#berapa total bunga dalam rupiah dan persen jika angsuran selama jangka waktu tersebut adalah total pinjaman beserta bunga?
#berapa bunga perbulan dalam rupiah dan persen?

#pinjam = pinjaman 
#angsur = angsuran per bulan
#waktu = jangka waktu 
#bunga_rp = bunga dalam rupiah
#bunga_persen = bunga dalam persen 
#bunga_rp_bulan = bunga dalam rupiah perbulan
#bunga_pr_bulan = bunga dalam rupah perbulan

# input =
# pinjaman , angsuran, jangka waktu
# proses = 
# total_angsur = angsur * waktu  
# total_bunga_rp = total_angsur - pinjam
# total_bunga_pr = total_bunga_rp / pinjam * 100         
# output = 
# hasil bunga dalam rupiah
# hasil bunga dalam persen 
# hasil bunga dalam rupiah perbulan
# hasil bunga dalam persen perbulan

#input
pinjam = int(input("Masukkan besar pinjaman (Rp.) ="))
angsur = int(input("Masukkan Angsuran perbulan (Rp.) ="))
waktu = int(input("Masukkan jangka waktu mengangsur ="))

#proses
total_angsur = angsur * waktu
total_bunga_rp = total_angsur - pinjam
total_bunga_pr = total_bunga_rp / pinjam * 100
bunga_bulan_rp = total_bunga_rp / waktu
bunga_bulan_pr = total_bunga_pr / waktu

#output
print("Total bunga dalam rupiah = Rp.",total_bunga_rp)
print("Total bunga dalam persen (%) = ","{:.0f}".format(total_bunga_pr),"%")
print("Total bunga dalam rupiah perbulan = Rp.","{:.0f}".format(bunga_bulan_rp)
print("Total bunga dalam persen perbulan (%) = ","{:.0f}".format(bunga_bulan_pr),"%")
