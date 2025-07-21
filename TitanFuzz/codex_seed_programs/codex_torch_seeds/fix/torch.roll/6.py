'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
import torch
input = torch.randn(3, 4, 5)
print('Input data: ', input)
output = torch.roll(input, shifts=2, dims=2)
print('Output data: ', output)