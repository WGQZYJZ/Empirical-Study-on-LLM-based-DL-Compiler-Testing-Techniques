'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
a = torch.randn(2, 3)
print(a)
b = torch.tile(a, (2, 2))
print(b)