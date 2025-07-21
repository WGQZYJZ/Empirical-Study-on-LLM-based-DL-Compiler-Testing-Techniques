'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input = torch.tensor([1, 2, 3])
output = torch.tile(input, (3, 1))
print(output)
output = torch.tile(input, (1, 3))
print(output)