# ระบบคลังข้อมูลและอัพเดตคลังข้อมูล pythainlp data

## หลักการและเหตุผล

เนื่องจาก PyThaiNLP มีการพัฒนาที่รวดเร็วมาก รวมถึงคลังข้อมูลที่มีการเปลี่ยนแปลงทุกครั้งที่ออกเวชั่นใหม่ จึงทำให้ต้องมีระบบอัพเดตและจัดเก็บอันใหม่ขึ้นมาเพื่อทดแทนระบบเดิม ชื่อ pythainlp-data

การพัฒนา

- ฐานข้อมูลในเครื่องผู้ใช้งานชื่อ db.json ใช้ tinydb
- ระเบียบคลังข้อมูลอยู่ที่  https://github.com/PyThaiNLP/pythainlp-corpus
- ใช้ tqdm แสดงสถานะการโหลด

## เรียกใช้งาน

```python
from pythainlp.corpus import download,get_file
```

## API

```python
get_file(ชื่อคลังข้อมูล)
```

ใช้สำหรับรับ path ที่ตั้งคลังข้อมูล (path ไฟล์หรือโฟลเดอร์)

เมื่อมีการเรียก api ชื่อ get_file(ชื่อคลังข้อมูล)

ระบบจะทำการเช็คในฐานข้อมูลที่อยู่ในเครื่องผู้ใช้งานว่ามีคลังข้อมูลนี้หรือไม่ ก็มีจะคืน path ที่ตั้งคลังข้อมูล แต่ถ้าไม่มีจะคืนค่า None ออกมา

```python
download(ชื่อคลังข้อมูล,force=False)
```

force คือการบังคับ ค่าพื้นฐานคือ False ถ้าเป็น True จะบังคับให้โหลดใหม่

การทำงาน

เมื่อเรียกใช้งานระบบจะทำการเช็คว่ามีคลังนี้ในระบบหรือไม่

ถ้ามี

- ระบบจะเช็คอีกว่าคลังข้อมูลมีเวชั่นใหม่หรือไม่ ถ้ามี จะมีขึ้นให้ input ว่าจะให้อัพเดตหรือไม่
- re-download ใหม่หรือไม่

ถ้าไม่มี

- จะโหลดให้เอง

ระบบจะอ้างอิงไฟล์ระเบียบคลังที่อยู่ที่ https://github.com/PyThaiNLP/pythainlp-corpus/blob/master/db.json

## ตัวอย่างการใช้งาน

```python
from pythainlp.corpus import get_file
from pythainlp.corpus import download

def download_path():
	path = get_file('thai2vec') # รับ path ที่ตั้งคลังข้อมูล
	if path==None: # ถ้าไม่พบ
		download('thai2vec') # ให้โหลด
		path = get_file('thai2vec') # รับ path ที่ตั้งคลังข้อมูล
	return path
```

