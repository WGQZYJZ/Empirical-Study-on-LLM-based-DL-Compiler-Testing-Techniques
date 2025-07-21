'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
input = torch.randn(1, 1, 5, 5)
output = nn.AdaptiveMaxPool2d((3, 3))(input)
print(output)
output = nn.AdaptiveMaxPool2d((3, 3), return_indices=True)(input)
print(output)