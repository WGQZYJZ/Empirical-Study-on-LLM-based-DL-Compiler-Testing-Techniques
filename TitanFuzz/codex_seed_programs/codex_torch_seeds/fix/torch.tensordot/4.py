'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensordot\ntorch.tensordot(a, b, dims=2, out=None)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[2, 3], [4, 5]])
print(torch.tensordot(a, b, dims=1))