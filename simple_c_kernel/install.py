import json
import os
import sys
from jupyter_client.kernelspec import KernelSpecManager

def main():
    kernel_json = {
        "argv": [sys.executable, "-m", "simple_c_kernel.kernel", "-f", "{connection_file}"],
        "display_name": "Simple C Kernel",
        "language": "c",
        "interrupt_mode": "signal"
    }

    kernel_spec_manager = KernelSpecManager()
    kernel_spec_manager.install_kernel_spec(
        kernel_name="simple_c_kernel",
        user=True,
        prefix=None
    )

    dest_dir = kernel_spec_manager.get_kernel_spec('simple_c_kernel')
    with open(os.path.join(dest_dir, 'kernel.json'), 'w') as f:
        json.dump(kernel_json, f, indent=4)

    print(f"✅ Simple C Kernel 설치 완료! (위치: {dest_dir})")

if __name__ == '__main__':
    main()