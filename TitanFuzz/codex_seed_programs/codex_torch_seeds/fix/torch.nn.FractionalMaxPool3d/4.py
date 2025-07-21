'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 2, 5, 5, 5)
pool = nn.FractionalMaxPool3d(2, output_size=[2, 2, 2])
output = pool(input_data)
print(output)
pool = nn.FractionalMaxPool3d(2, output_ratio=[0.5, 0.5, 0.5])
output = pool(input_data)
print(output)