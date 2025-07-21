'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 7, 7, 7)
output_data = nn.FractionalMaxPool3d(kernel_size=(3, 3, 3), output_size=(4, 4, 4))(input_data)
print('output_data.size() = ', output_data.size())
print('output_data = \n', output_data)