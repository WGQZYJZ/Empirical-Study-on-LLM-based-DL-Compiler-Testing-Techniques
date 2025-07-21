'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[7, 8], [9, 10], [11, 12]])
res = torch.kron(input, other)
print(res)
print(res.size())