'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = torch.randn(2, 3)
print(input_data)
dropout = nn.Dropout(p=0.5)
output = dropout(input_data)
print(output)
dropout = nn.Dropout(p=0.5, inplace=True)
output = dropout(input_data)
print(output)