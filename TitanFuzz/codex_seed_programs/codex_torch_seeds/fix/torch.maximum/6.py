'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
y = torch.tensor([1, 2, 1, 2, 1], dtype=torch.float32)
print(torch.maximum(x, y))
print(torch.min(x, y))