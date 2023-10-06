# 寫一程式程式以實作 1.6節 所提的植基於位元平面之浮水印

## Assignment Description
上課課本章節 1.9作業 第4題(第七版課本p. 25)，"寫一程式程式以實作 1.6節 所提的植基於位元平面之浮水印"。
程式的
輸入圖片有兩張，原圖及嵌入浮水印必須為兩張明顯不同的的 "同學自拍照" (都為灰階圖即可)，
輸出圖片有兩張，(1)對原圖分別把 8bit  去掉 least significant X bits(X為同學的學號最後一位數餘4加1)，並嵌入浮水印輸出，(2)再從該圖還原出所嵌入的浮水印輸出。

請各位同學以 C++/python/matlab撰寫程式，並繳交專案程式檔(C++需有exe檔)、4張圖片檔(含輸入、輸出)及執行說明檔(readme，可與後面PDF撰寫在一起)，
另外必須再繳交一份含程式、程式註解及實作前後結果圖之PDF檔，
請將要繳交的項目打包成 zip、7z檔 上傳至moodle，資料夾名稱設為名稱為 學號_姓名(ex: M110XXXXX_劉XX)。


## Install requirements
    $ pip install -r requirement.txt

## How to run 
### Step 1. Prepare two selfies
The first selfie will be embedded, and the second selfie will embedded into the first one.\

**CAUTION** : the size of the second selfie must be larger than that of the first selfie.
### Step 2.
Find your last digit of your last student ID.
### Step 3. Open main.py
### Step 4. Find the line and change the input image path
    input_image_path = 'selfie1.jpg' #被嵌入圖片路徑
### Step 5. Find the line and change watermark image path
    watermark_image_path = 'selfie2.jpg' #浮水印圖片路徑
### Step 6. Find the line and change the number to your last digit of student ID
    last_ID_number = 1 #學號最後一位數字 M11202151
### Step 7.  Open terminal and execute these two command
    $ cd ./to-the-watermark-directory
    $ python main.py
### Step 8. Find your output images
The embedded image is named "embedded_image.png".\
The extracted watermark image is named "extracted_watermark.png"\
These two photos are stored in the same folder as main.py.
### Step 9. Finish