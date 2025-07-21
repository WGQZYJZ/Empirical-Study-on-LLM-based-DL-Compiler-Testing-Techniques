'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(10, 10)
torch.nn.Hardswish(inplace=False)
print(input_data)