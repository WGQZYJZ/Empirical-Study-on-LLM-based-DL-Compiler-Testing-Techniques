'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
input = torch.arange(24)
input = input.view(2, 3, 4)
print('Input: ', input)
output = torch.roll(input, shifts=1, dims=1)
print('Output: ', output)