'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(20, 16, 50, 32, 45)
print('Task 3: Call the API torch.nn.FractionalMaxPool3d')
pool = nn.FractionalMaxPool3d(3, output_size=(5, 7, 11))
output = pool(input)
print('Task 4: Print output size')
print(output.size())