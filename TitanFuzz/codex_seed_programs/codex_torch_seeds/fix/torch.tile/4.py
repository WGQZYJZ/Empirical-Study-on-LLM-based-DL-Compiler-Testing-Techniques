'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
import torch
input = torch.arange(1, 4)
print('Input: ', input)
output = torch.tile(input, (2, 2))
print('Output: ', output)