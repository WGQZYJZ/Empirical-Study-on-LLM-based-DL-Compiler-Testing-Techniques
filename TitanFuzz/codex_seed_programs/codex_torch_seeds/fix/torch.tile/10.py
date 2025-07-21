'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input = torch.arange(1, 4, dtype=torch.float32)
print('input: ', input)
output = torch.tile(input, (2, 1))
print('output: ', output)