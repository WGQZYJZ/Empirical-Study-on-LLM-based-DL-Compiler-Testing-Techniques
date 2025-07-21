'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 224, 224)
import torch
input_data = torch.randn(1, 3, 224, 224)
hardswish = nn.Hardswish(inplace=False)
output = hardswish(input_data)
print(output)