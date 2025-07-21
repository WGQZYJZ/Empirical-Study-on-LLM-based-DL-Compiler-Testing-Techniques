'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input = torch.arange(1, 11)
input = input.view(2, 5)
print('input: ', input)
reps = (2, 3)
output = torch.tile(input, reps)
print('output: ', output)