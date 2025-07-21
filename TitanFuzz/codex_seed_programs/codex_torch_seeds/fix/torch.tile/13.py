'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input = torch.arange(1, 11)
input = input.view(1, 10)
output = torch.tile(input, (3, 1))
print('Input: ', input)
print('Output: ', output)