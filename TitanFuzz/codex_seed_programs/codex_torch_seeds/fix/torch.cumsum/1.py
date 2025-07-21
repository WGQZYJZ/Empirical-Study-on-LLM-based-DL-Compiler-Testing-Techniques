'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6])
print(torch.cumsum(x, dim=0))
print(torch.cumsum(x, dim=0, dtype=torch.float))
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(torch.cumsum(x, dim=0))
print(torch.cumsum(x, dim=1))