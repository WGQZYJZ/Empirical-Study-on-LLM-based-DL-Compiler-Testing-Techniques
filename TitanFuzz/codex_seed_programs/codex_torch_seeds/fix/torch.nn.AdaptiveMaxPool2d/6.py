'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 5, 5)
print('input_data:\n', input_data)
output = nn.AdaptiveMaxPool2d((2, 2))(input_data)
print('output:\n', output)
(output, indices) = nn.AdaptiveMaxPool2d((2, 2), return_indices=True)(input_data)