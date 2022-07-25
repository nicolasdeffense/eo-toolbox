import subprocess, glob
from pathlib import Path

grp = 'U'
prod_type = 'S2_MSIL1C'

input_dir  = f'/scratch/ndeffense/dwl_student/GROUP_{grp}/{prod_type}/'
output_dir = f'/scratch/ndeffense/dwl_student/GROUP_{grp}/{prod_type}/'
zip_done_dir  = f'{input_dir}zip_done/'
safe_done_dir = f'{input_dir}safe_done/'

Path(safe_done_dir).mkdir(parents=True, exist_ok=True)


cloud_proba = -10

for safe_file in glob.glob(f'{input_dir}*.SAFE'):

    cmd = 'Fmask'
    cmd += f' --proba {cloud_proba}'
    cmd += f' --outdir {output_dir}'
    cmd += f' {safe_file}'
    
    print(cmd)
    
    subprocess.call(cmd, shell=True)
    
    cmd = f'mv {safe_file} {safe_done_dir}'
    
    print(cmd)
    
    subprocess.call(cmd, shell=True)






'''
for zip_file in glob.glob(f'{input_dir}*.zip'):
        
    cmd = f'unzip {zip_file} -d {input_dir}'
    
    print(cmd)
    
    subprocess.call(cmd, shell=True)

    cmd = 'Fmask'
    cmd += f' --proba {cloud_proba}'
    cmd += f' --outdir {output_dir}'
    cmd += f' {zip_file[:-4]}.SAFE'
    
    print(cmd)
    
    subprocess.call(cmd, shell=True)
    
    cmd = f'mv {zip_file} {zip_done_dir}'
    
    print(cmd)
    
    subprocess.call(cmd, shell=True)
'''