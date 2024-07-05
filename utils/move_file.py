import os
import shutil
import concurrent.futures


def collect_images(source_dirs, destination_dir):
    # Tạo thư mục đích nếu chưa tồn tại
    os.makedirs(destination_dir, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Lặp qua các thư mục nguồn và gửi các nhiệm vụ (task) cho các luồng (threads)
        futures = [executor.submit(
            copy_images, source_dir, destination_dir) for source_dir in source_dirs]

        # Chờ tất cả các nhiệm vụ hoàn thành
        concurrent.futures.wait(futures)


def copy_images(source_dir, destination_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Kiểm tra loại file (ảnh)
            if file.endswith(('.jpg', '.jpeg', '.png')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, file)
                # Sao chép file vào thư mục đích
                shutil.copy(source_path, destination_path)


# Sử dụng ví dụ:
source_dirs = ['data\C\C45', 'data\C\C46', 'data\C\C47', 'data\C\C48', 'data\C\C49', 'data\C\C50', 'data\C\C51', 'data\C\C52',
               'data\C\C53', 'data\C\C54', 'data\C\C55', 'data\C\C56', 'data\C\C57', 'data\C\C58', 'data\C\C59', 'data\C\C60']
destination_dir = 'C45_C60'

collect_images(source_dirs, destination_dir)
# import os
# import random
# import shutil

# # Đường dẫn đến thư mục lớn chứa các thư mục nhỏ
# large_directory = 'data/C'

# # Đường dẫn đến thư mục lớn để chứa tất cả các ảnh
# target_directory = 'C_test'

# # Lặp qua từng thư mục nhỏ trong thư mục lớn
# for subdir in os.listdir(large_directory):
#     subdir_path = os.path.join(large_directory, subdir)

#     # Kiểm tra xem đối tượng có phải là thư mục hay không
#     if os.path.isdir(subdir_path):
#         # Lấy danh sách tất cả các tệp tin ảnh trong thư mục nhỏ
#         image_files = [file for file in os.listdir(subdir_path) if file.endswith('.jpeg') or file.endswith('.png')]

#         # Lấy ngẫu nhiên hai ảnh từ danh sách ảnh
#         random_images = random.sample(image_files, 2)

#         # Di chuyển các ảnh vào thư mục lớn
#         for image in random_images:
#             image_path = os.path.join(subdir_path, image)
#             target_path = os.path.join(target_directory, image)
#             shutil.copy(image_path, target_path)
