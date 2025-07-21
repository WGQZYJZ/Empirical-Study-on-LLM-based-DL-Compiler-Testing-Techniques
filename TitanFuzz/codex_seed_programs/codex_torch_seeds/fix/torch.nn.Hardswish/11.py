'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 2, 2)
hardswish = nn.Hardswish(inplace=False)
output = hardswish(input_data)
print(output)