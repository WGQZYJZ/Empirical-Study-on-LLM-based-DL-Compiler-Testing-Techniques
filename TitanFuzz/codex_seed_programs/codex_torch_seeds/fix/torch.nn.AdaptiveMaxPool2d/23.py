'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
input = torch.randn(1, 1, 3, 3)
output = nn.AdaptiveMaxPool2d(output_size=(1, 1))(input)
print(output)
output = nn.AdaptiveMaxPool2d(output_size=(3, 3))(input)
print(output)