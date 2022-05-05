import subprocess, glob

input_dir  = '/scratch/ndeffense/dwl_student/GROUP_N/'
output_dir = '/scratch/ndeffense/dwl_student/GROUP_N/'
zip_done_dir  = '/scratch/ndeffense/dwl_student/GROUP_N/zip_done/'
safe_done_dir = '/scratch/ndeffense/dwl_student/GROUP_N/safe_done/'


cloud_proba = 20

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