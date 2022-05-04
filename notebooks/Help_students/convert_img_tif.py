import subprocess


input_im = '/export/miro/students/bnorgaard/Backup_training_data/images/Subset_S2B_MSIL2A_20200601T103629_N0214_R008_T31UFS_20200601T135554_resampled_BandMath.data/lai.img'

output_tif = '/export/miro/ndeffense/lai_20200601.tif'


cmd = 'gdal_translate'
cmd += ' -of GTiff'
cmd += ' ' + input_im
cmd += ' ' + output_tif

print(cmd)

subprocess.call(cmd, shell=True)

