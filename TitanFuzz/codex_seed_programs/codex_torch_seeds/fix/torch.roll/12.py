'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
print('Output: ', torch.roll(input, shifts=1, dims=1))