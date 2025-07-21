'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
input = torch.randn(3, 20)
print('Input data: ', input)
split_tensor = torch.hsplit(input, [15, 18])
print('Output data: ', split_tensor)