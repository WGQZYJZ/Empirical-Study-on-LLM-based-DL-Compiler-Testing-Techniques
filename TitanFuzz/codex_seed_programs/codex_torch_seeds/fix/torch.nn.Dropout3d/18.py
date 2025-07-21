'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout3d\ntorch.nn.Dropout3d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(4, 3, 10, 10, 10)
dropout3d = nn.Dropout3d(p=0.5, inplace=False)
output = dropout3d(input_data)
print(output)