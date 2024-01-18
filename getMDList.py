import os
import json

# 取得當前文件夾的路徑
current_folder = os.getcwd()

# 要檢查的目錄路徑
posts_folder = os.path.join(current_folder, 'contents', 'posts')

# 取得當前文件夾中所有以.md結尾的檔案
md_files = [file for file in os.listdir(posts_folder) if file.endswith('.md')]


# 將檔案列表轉換為JSON格式
json_output = json.dumps(md_files, indent=2)

# 將JSON寫入到檔案中
with open("mdlist.json", "w") as json_file:
    json_file.write(json_output)

print("整理完成，結果已輸出到 output.json 檔案。")
