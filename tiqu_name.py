import os
import pandas as pd

def list_files_in_current_directory():
    # 获取当前目录
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")
    
    # 列出当前目录下的所有文件和文件夹
    items = os.listdir(current_directory)
    
    # 过滤出文件
    files = [item for item in items if os.path.isfile(os.path.join(current_directory, item))]
    
    return files

def save_to_excel(file_names, output_file='file_names.xlsx'):
    # 创建一个DataFrame
    df = pd.DataFrame(file_names, columns=['File Name'])
    
    # 将DataFrame保存到Excel文件
    df.to_excel(output_file, index=False)
    print(f"File names have been saved to {output_file}")

if __name__ == "__main__":
    files = list_files_in_current_directory()
    print("Files in the current directory:")
    for file in files:
        print(file)
    
    # 保存文件名到Excel
    save_to_excel(files)
