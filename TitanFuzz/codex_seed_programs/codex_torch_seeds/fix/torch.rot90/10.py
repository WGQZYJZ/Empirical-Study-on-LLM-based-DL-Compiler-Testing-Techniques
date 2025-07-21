'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input = torch.arange(0, 16, dtype=torch.float).view(4, 4)
print('Input: \n', input)
output = torch.rot90(input, 1, (0, 1))
print('Output: \n', output)