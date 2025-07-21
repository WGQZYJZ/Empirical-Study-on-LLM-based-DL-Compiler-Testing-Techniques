'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(1, 3, 5, 5)
pool = nn.AdaptiveAvgPool2d(output_size=(1, 1))
output = pool(input_data)
print(output)