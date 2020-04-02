import os
import pandas as pd
import shutil

if '1_sam' not in os.listdir():
    os.mkdir('1_sam')
if '0_sam' not in os.listdir():
    os.mkdir('0_sam')

df = pd.read_excel('celegans_labels.xlsx')
df = df.set_index('Image')
# df.info()
for img in os.listdir('celegans_training_set_super_cropped/'):
    num = int(img.split('.')[0].split('_')[1])
    if num < 5731:
        continue
    hasworm = df.loc[num,'Worm']
    if hasworm == 1:
        shutil.copy('celegans_training_set_super_cropped/'+img,'1_sam/'+img)
    else:
        shutil.copy('celegans_training_set_super_cropped/'+img,'0_sam/'+img)