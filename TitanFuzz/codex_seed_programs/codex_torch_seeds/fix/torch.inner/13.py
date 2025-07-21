'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inner\ntorch.inner(input, other, *, out=None)\n'
import torch
a = torch.tensor([1, 2, 3, 4, 5])
b = torch.tensor([1, 2, 3, 4, 5])
print(torch.inner(a, b))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6]])
b = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(torch.matmul(a, b))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6]])