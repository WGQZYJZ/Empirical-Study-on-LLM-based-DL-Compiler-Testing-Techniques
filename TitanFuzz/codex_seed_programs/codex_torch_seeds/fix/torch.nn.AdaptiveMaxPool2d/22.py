'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch
input = torch.randn(1, 1, 4, 4)
print('Input:\n', input)
output = torch.nn.AdaptiveMaxPool2d((3, 3))(input)
print('Output:\n', output)