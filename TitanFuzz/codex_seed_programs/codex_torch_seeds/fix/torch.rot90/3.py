'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.arange(0, 60).view(3, 4, 5)
print('Input data: \n', input)
input = torch.arange(0, 60).view(3, 4, 5)
output = torch.rot90(input, 1, dims=(0, 1))
print('Output data: \n', output)