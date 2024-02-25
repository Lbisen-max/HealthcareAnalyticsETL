import os
import shutil

from src.main.ProjectConfig import ProjectConfig,ProjectSchema
from src.main.utility.s3_client_object import *
# def Seprate_csv_file_to_local(local_directory):
#     for main_dir,sub_dir,files in os.walk(ProjectConfig.local_directory):
#         for file in files:
#             if file.endswith(".csv"):
#                 file_path = os.path.join(main_dir, file)
#                 # shutil.copy(file_path, ProjectConfig.destination_path)
#

# for x,y,z in os.walk(ProjectConfig.destination_path):
#     print(x)
#     print(z)




