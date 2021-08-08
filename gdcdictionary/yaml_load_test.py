'''
One yaml file could not be encoded correctly.
The current tests do not pinpoint which yaml file
is causing issue. Therefore, I made a script to 
see which yaml files are not loading properly
(and subsequently causing importing gdcdictionary module)
'''

#%%
import dictionaryutils as dictutils
import os
import glob

import yaml

# %%
schema_yaml_list = glob.glob('schemas/*.yaml')
# %%
#see if there are any errors
for yaml_file in schema_yaml_list:
    try:
        dictutils.load_yaml(yaml_file)
        print(f"[successful load] {yaml_file}")
    except UnicodeError as e: 
        print(f"[unsuccesful load] {yaml_file}\n{e}")
# %%
