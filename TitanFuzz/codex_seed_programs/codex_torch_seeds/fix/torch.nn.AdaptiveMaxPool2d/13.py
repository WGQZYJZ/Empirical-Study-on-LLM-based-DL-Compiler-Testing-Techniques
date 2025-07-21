'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 6, 6)
output = nn.AdaptiveMaxPool2d(output_size=(2, 2))(input)
print(output)