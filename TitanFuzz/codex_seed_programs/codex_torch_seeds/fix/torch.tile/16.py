'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input = torch.arange(1, 11)
reps = (2, 5)
output = torch.tile(input, reps)
print('Input: ', input)
print('Output: ', output)