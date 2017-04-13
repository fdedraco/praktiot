from xbee import ZigBee
from xbee.helpers.dispatch import Dispatch
import serial
import struct
import datetime
import time

# Define which port to use
PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)
xbee = ZigBee(ser,escaped=True)

response = xbee.wait_read_frame()
sourceAddrLong = hex(response["source_addr_long"])

if response["id"] == "rx":
	if response["rf_data"][0:1] == "0":
		print "Ada Kendaraaan"
		
noRegistrasi = response["rf_data"][1:11]
namaPemilik = response["rf_data"][11:31]
alamat = response["rf_data"][31:81]
isiSilinder = response["rf_data"][81:85]
noRangka = response["rf_data"][85:102]
noMesin = response["rf_data"][102:116]
tahunRegistrasi = response["rf_data"][121:125]
berlakuSampaiTgl = response["rf_data"][125:127]
berlakuSampaiBln = response["rf_data"][127:129]
berlakuSampaiThn = response["rf_data"][129:133]
noBPKB = response["rf_data"][133:]

WMI = response["rf_data"][85:88]
 # merk =
if WMI == "MH1":
	merk = "HONDA"
elif WMI == "MH3":
	merk = "YAMAHA"
elif WMI == "MH8":
	merk = "SUZUKI"
elif WMI == "MHF":
	merk = "TOYOTA"
elif WMI == "MKD":
	merk = "MINERVA"
 
 VDS = response["rf_data"][88:94]
 # tipe =
if VDS == "1PA002":
	tipe = "VNL 2013"
elif VDS == "BG41CA":
	tipe = "SATRIA FU 150"
elif VDS == "KC3115C":
	tipe = "MEGA PRO CW"
elif VDS =="ZX69G"
	tipe = "T. FORTUNER 2.7 G AT"
elif VDS == "JB211":
	tipe = "HONDA NF 125"
 
codeYear = response["rf_data"][94:95]
# tahunPembuatan =
if codeYear == "4":
	tahunPembuatan = "2004"
elif codeYear == "A":
	tahunPembuatan = "2010"
elif codeYear == "B":
	tahunPembuatan = "2011"
elif codeYear == "C":
	tahunPembuatan = "2012"
 
codeJenis = response["rf_data"][116:117]
# jenis =
if codeJenis == "1":
	jenis = "SEPEDA MOTOR"
elif codeJenis == "2":
	jenis = "MOBIL PENUMPANG"
codeModel = response["rf_data"][117:118]
# model =
if codeModel == "1":
	model = "SEPEDA MOTOR SOLO"
elif codeModel == "2":
	model = "MICRO/MINIBUS"
elif codeModel == "3":
	model = "SEDAN"
codeWarna = response["rf_data"][118:119]
# warna =
if codeWarna == "0":
	warna = "HITAM"
elif codeWarna == "1":
	warna = "COKELAT"
elif codeWarna == "2":
	warna = "MERAH"
elif codeWarna == "3":
	warna = "JINGGA"
elif codeWarna == "4":
	warna = "KUNING"
codeBahanBakar = response["rf_data"][119:120]
# bahanBakar =
if codeBahanBakar == "1":
	bahanBakar = "PREMIUM"
elif codeBahanBakar == "2":
	bahanBakar = "PERTAMAX"
elif codeBahanBakar == "3":
	bahanBakar = "PERTAMAX PLUS"
elif codeBahanBakar == "4":
	bahanBakar = "PERTALITE"
elif codeBahanBakar == "5":
	bahanBakar = "SOLAR"
codeWarnaTNKB = response["rf_data"][120:121]
# warnaTNKB =
if codeWarnaTNKB == "1":
	warnaTNKB = "HITAM"
elif codeWarnaTNKB == "2":
	warnaTNKB = "PUTIH"
elif codeWarnaTNKB == "3":
	warnaTNKB = "MERAH"