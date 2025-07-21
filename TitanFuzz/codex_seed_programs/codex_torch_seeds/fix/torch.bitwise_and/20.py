'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
a = torch.tensor([0, 1, 0, 1], dtype=torch.uint8)
b = torch.tensor([1, 0, 1, 0], dtype=torch.uint8)
print(torch.bitwise_and(a, b))