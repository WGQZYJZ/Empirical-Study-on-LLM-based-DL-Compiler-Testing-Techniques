'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_1d\ntorch.atleast_1d(*tensors)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([[1, 2, 3], [4, 5, 6]])
c = torch.tensor([1, 2, 3], dtype=torch.float)
d = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
print(torch.atleast_1d(a))
print(torch.atleast_1d(b))
print(torch.atleast_1d(c))
print(torch.atleast_1d(d))