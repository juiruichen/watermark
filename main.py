import cv2
import numpy as np

def embed_watermark(input_image_path, watermark_image_path, output_image_path, last_ID_number):
    
    number_of_bit = last_ID_number % 4 + 1 #學號最後一位數餘4加1
    filterA = int('1'*(8-number_of_bit) + '0'*(number_of_bit), 2) #0b11111100
    filterB = int('1'*(number_of_bit) + '0'*(8-number_of_bit), 2) #0b11000000

    #TODO: 讀取照片並轉為灰階照片 格式為uint8
    input_image = cv2.cvtColor(cv2.imread(input_image_path).astype('uint8'), cv2.COLOR_BGR2GRAY)
    watermark_image = cv2.cvtColor(cv2.imread(watermark_image_path).astype('uint8'), cv2.COLOR_BGR2GRAY)

    height, width = input_image.shape
    if height>watermark_image.shape[0] or width>watermark_image.shape[1]:
        raise Exception(f"被嵌入圖片({input_image.shape})的高或寬大於浮水印({watermark_image.shape})，無法嵌入浮水印")
    watermark_image = cv2.resize(watermark_image, (width, height))
    embeded_image = np.zeros((height, width), dtype='uint8')

    for h in range(height):
        for w in range(width):
            embeded_image[h][w] = input_image[h][w] & filterA
            tmp = watermark_image[h][w] & filterB
            tmp >>= 8-number_of_bit
            embeded_image[h][w] |= tmp
    
    cv2.imwrite(output_image_path, embeded_image)


def extract_watermark(embeded_image_path, output_watermark_path, last_ID_number):

    number_of_bit = last_ID_number % 4 + 1 #學號最後一位數餘4加1
    bin_filter = int('0'*(8-number_of_bit) + '1'*(number_of_bit), 2) #0b00000011

    #TODO: 讀取照片並轉為灰階照片 格式為uint8
    embeded_image = cv2.cvtColor(cv2.imread(embeded_image_path).astype('uint8'), cv2.COLOR_BGR2GRAY)
    height, width = embeded_image.shape
    
    watermark = np.zeros((height, width), dtype='uint8')
    for h in range(height):
        for w in range(width):
            tmp = embeded_image[h][w] & bin_filter
            tmp <<= 8-number_of_bit
            watermark[h][w] |= tmp
    
    cv2.imwrite(output_watermark_path, watermark)


if __name__ == '__main__':

    #TODO: Enter parameters
    input_image_path = 'selfie1.jpg' #被嵌入圖片路徑
    watermark_image_path = 'selfie2.jpg' #浮水印圖片路徑
    last_ID_number = 1 #學號最後一位數字 M11202151

    #TODO: 植入浮水印
    embeded_image_path = 'embedded_image.png' #被嵌入浮水印圖片的儲存路徑
    embed_watermark(input_image_path, watermark_image_path, embeded_image_path, last_ID_number)

    #TODO: 取出浮水印
    extracted_watermark_path = 'extracted_watermark.png' #取出浮水印圖片的儲存路徑
    extract_watermark(embeded_image_path, extracted_watermark_path, last_ID_number)