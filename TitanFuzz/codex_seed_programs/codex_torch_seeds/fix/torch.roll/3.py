'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
input = torch.randn(2, 3, 4)
print('Input: ', input)
output = torch.roll(input, shifts=2, dims=1)
print('Output: ', output)