'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
print(torch.log1p(x))
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
print(torch.log1p(x))
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float64)
print(torch.log1p(x))