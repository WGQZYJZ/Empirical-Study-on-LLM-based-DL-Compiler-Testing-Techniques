'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.ones(100, 100)
dropout = nn.Dropout2d(p=0.5, inplace=False)
output = dropout(input_data)
print(output)