'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(1, 1, 4, 4)
print('Task 3: Call the API torch.nn.AdaptiveMaxPool2d')
output = torch.nn.AdaptiveMaxPool2d((2, 2))(input)
print('output = ', output)