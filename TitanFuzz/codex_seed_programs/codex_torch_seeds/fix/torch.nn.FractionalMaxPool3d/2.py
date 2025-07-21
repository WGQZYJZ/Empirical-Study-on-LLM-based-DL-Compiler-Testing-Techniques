'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 5, 7, 9)
pool = nn.FractionalMaxPool3d(2, output_size=[2, 3, 4])
output = pool(input)
print(output)