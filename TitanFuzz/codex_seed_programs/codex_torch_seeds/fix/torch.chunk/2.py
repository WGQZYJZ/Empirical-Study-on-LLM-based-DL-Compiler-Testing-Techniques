'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
import torch
input = torch.randn(20)
output = torch.chunk(input, 4)
print('Input size: ', input.size())
print('Output size: ', output[0].size())