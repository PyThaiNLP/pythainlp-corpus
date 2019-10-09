# ระบบคลังข้อมูล PyThaiNLP Data

## หลักการและเหตุผล

เนื่องจาก PyThaiNLP มีการพัฒนาที่รวดเร็วมาก รวมถึงคลังข้อมูลที่มีการเปลี่ยนแปลงทุกครั้งที่ออกรุ่นใหม่ จึงทำให้ต้องมีระบบปรับปรุงและจัดเก็บอันใหม่ขึ้นมาเพื่อทดแทนระบบเดิม ชื่อ pythainlp-data

การพัฒนา

- ฐานข้อมูลในเครื่องผู้ใช้งานชื่อ db.json ใช้ TinyDB
- ระเบียบคลังข้อมูลอยู่ที่  https://github.com/PyThaiNLP/pythainlp-corpus
- ใช้ tqdm แสดงสถานะการโหลด
- ที่ตั้งของโฟลเดอร์ pythainlp-data อยู่ที่ ~ หรือโฟลเดอร์หลักของผู้ใช้ โฟลเดอร์ pythainlp-data เป็นที่เก็บคลังและ db.json

## เรียกใช้งาน

```python
from pythainlp.corpus import download, get_file
```

## API

### รับ path คลังข้อมูล

```python
get_file(ชื่อคลังข้อมูล)
```

ใช้สำหรับรับ path ที่ตั้งคลังข้อมูล (path ไฟล์หรือโฟลเดอร์)

เมื่อมีการเรียก api ชื่อ get_file(ชื่อคลังข้อมูล)

ระบบจะทำการเช็คในฐานข้อมูลที่อยู่ในเครื่องผู้ใช้งานว่ามีคลังข้อมูลนี้หรือไม่ ก็มีจะคืน path ที่ตั้งคลังข้อมูล แต่ถ้าไม่มีจะคืนค่า None ออกมา

### โหลดคลังข้อมูล

```python
download(ชื่อคลังข้อมูล, force=False)
```

force คือการบังคับ ค่าปริยายคือ False ถ้าเป็น True จะบังคับให้โหลดใหม่

การทำงาน

เมื่อเรียกใช้งานระบบจะทำการเช็คว่ามีคลังนี้ในระบบหรือไม่

ถ้ามี

- ระบบจะตรวจสอบอีกว่าคลังมีข้อมูลรุ่นใหม่หรือไม่ ถ้ามี จะถามผู้ใช้ว่าจะให้ปรับเป็นรุ่นใหม่หรือไม่
- ดาวน์โหลดซ้ำหรือไม่

ถ้าไม่มี

- จะโหลดให้เองอัตโนมัติ

ระบบจะอ้างอิงไฟล์ระเบียบคลังที่อยู่ที่ https://github.com/PyThaiNLP/pythainlp-corpus/blob/master/db.json

#### ตัวอย่างการใช้งาน

```python
from pythainlp.corpus import download, get_file

def download_path():
	path = get_file('thai2vec')  # รับ path ที่ตั้งคลังข้อมูล
	if not path:  # ถ้าไม่พบ
		download('thai2vec')  # ให้โหลด
		path = get_file('thai2vec')  # รับ path ที่ตั้งคลังข้อมูล
	return path
```

### รับข้อมูลรายละเอียดคลังข้อมูลที่อยู่ในเครื่อง

```python
>>> from pythainlp.corpus import *
>>> get_corpus_db_detail("thainer")
{'name': 'thainer', 'version': '1.1', 'file': 'thainer.model'}
