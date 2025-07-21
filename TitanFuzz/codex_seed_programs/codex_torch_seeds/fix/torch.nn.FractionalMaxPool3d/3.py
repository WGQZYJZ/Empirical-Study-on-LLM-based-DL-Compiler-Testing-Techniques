'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 16, 50, 32, 45)
m = nn.FractionalMaxPool3d(3, output_size=(4, 4, 4))
output = m(input)
print(output.size())