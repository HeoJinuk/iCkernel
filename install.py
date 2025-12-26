import json
import os
import sys
from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory
import shutil

kernel_name = "simple_c_kernel"
kernel_display_name = "Simple C Kernel"

def install_my_kernel_spec(user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755) # 권한 설정
        
        # 1. 현재 폴더의 kernel.py와 kernel.json을 임시 폴더로 복사
        source_dir = os.path.dirname(os.path.abspath(__file__))
        shutil.copy(os.path.join(source_dir, 'kernel.py'), os.path.join(td, 'kernel.py'))
        shutil.copy(os.path.join(source_dir, 'kernel.json'), os.path.join(td, 'kernel.json'))

        # 2. 주피터 커널 설치 (자동으로 시스템 경로에 복사됨)
        print(f"Installing {kernel_display_name}...")
        KernelSpecManager().install_kernel_spec(td, kernel_name, user=user, prefix=prefix)
        print(f"설치 완료! Jupyter Notebook을 새로고침 하세요.")

if __name__ == '__main__':
    install_my_kernel_spec()