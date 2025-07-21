'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = torch.randn(1, 2, 6, 6, 6)
fractional_max_pool3d = nn.FractionalMaxPool3d(kernel_size=(2, 2, 2), output_size=(4, 4, 4))
output_data = fractional_max_pool3d(input_data)
print('input_data:', input_data)
print('output_data:', output_data)