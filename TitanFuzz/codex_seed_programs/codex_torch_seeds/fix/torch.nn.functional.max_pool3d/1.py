'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool3d\ntorch.nn.functional.max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import numpy as np
input_data = torch.arange(0, 27).view(1, 1, 3, 3, 3)
input_data = input_data.float()
output = torch.nn.functional.max_pool3d(input_data, kernel_size=2, stride=2)
print(output)