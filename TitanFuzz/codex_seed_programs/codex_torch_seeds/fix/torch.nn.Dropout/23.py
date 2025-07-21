'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 28, 28)
print(input_data.shape)
dropout = nn.Dropout(p=0.5, inplace=False)
output = dropout(input_data)
print(output.shape)