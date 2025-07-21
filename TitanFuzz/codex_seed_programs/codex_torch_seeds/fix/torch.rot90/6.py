'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.arange(24).view(2, 3, 4)
output = torch.rot90(input, 1, dims=(1, 2))
print('Input:')
print(input)
print('Output:')
print(output)