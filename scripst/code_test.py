# %%
import os
import sys
import platform
print(platform.python_version())
print(sys.path)
# %%
# data = os.listdir('../data')
# print(data)

from datasets import list_datasets, load_dataset, list_metrics, load_metric

# Print all the available datasets
print(list_datasets())
# %%
