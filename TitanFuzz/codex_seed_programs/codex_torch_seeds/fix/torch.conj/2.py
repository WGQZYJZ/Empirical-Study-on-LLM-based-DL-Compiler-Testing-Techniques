'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj\ntorch.conj(input)\n'
import torch
input = torch.rand(1, 2, 3, 4)
print('Input: ', input)
output = torch.conj(input)
print('Output: ', output)