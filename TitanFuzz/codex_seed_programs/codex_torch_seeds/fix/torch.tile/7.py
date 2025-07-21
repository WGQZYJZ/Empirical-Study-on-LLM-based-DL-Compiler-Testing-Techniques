'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
x = torch.randn(1, 3)
print(x)
print(torch.tile(x, (2, 1)))
print(torch.tile(x, (2, 2)))
print(torch.tile(x, (2, 3)))
print(torch.tile(x, (3, 3)))