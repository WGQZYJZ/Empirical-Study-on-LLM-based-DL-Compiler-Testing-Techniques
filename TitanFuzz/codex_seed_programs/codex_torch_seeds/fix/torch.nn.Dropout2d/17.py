'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(1, 3, 3, 3)
dropout = nn.Dropout2d(p=0.5, inplace=False)
output = dropout(input_data)
print('Input data: \n', input_data)
print('Output: \n', output)