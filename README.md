[doaw load model from here ](https://drive.google.com/drive/folders/1AXOT72URLVdg6kTIm3d0Iq6-EYi6Q8Sd?usp=sharing)

# Predicting orange sugar from images

Note: đầu vào của api có thể cho vào nhiều ảnh hoặc nén vào 1 file zip và upload 1 lần !
![input](data/image/image_1_5.jpeg)

Dưới đây là một ví dụ README hướng dẫn chạy API này:

# Hướng dẫn chạy API

## Cài đặt

1. Cài đặt Python (phiên bản 3.7 trở lên).

2. Cài đặt các thư viện cần thiết bằng lệnh sau:

   ```bash
   pip install requirements.txt
   ```

## Chạy API

1. Clone repository từ GitHub:

   ```bash
   git clone https://github.com/Nguyendai202/Predicting-orange-sugar-from-images.git
   ```

2. Di chuyển vào thư mục chứa mã nguồn:

   ```bash
   cd your-repo
   ```

3. Chạy API bằng lệnh sau:

   ```bash
   python _api_.py
   ```

4. API sẽ chạy trên `http://127.0.0.1:8000`.

   
   ![input_file](input.png)

5. Sau khi ấn Choose File, nhập file của bạn vào và ấn Execute thì lướt xuống dưới sẽ có kết quả ở đây
   
![result](result.png)

## Sử dụng API

API này chỉ có một endpoint `/docs` nhận một hoặc nhiều ảnh làm tham số đầu vào và đầu ra là 1 số thực đại diện cho mục tiêu của bài toán là độ đường



### Request

- Phương thức: POST
- Endpoint: `http://127.0.0.1:8000/docs`
- Header: không yêu cầu
- Body:
  - Loại: form-data
  - Key: `image`


### Response

Loại: float






