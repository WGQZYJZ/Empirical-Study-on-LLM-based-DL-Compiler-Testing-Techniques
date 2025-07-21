'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input = torch.arange(0, 9, dtype=torch.float32)
input = input.view(3, 3)
print('input:', input)
reps = (2, 2)
output = torch.tile(input, reps)
print('output:', output)