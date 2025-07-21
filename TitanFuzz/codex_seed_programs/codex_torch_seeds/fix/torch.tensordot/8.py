'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensordot\ntorch.tensordot(a, b, dims=2, out=None)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
c = torch.tensor([[9, 10], [11, 12]])
d = torch.tensor([[13, 14], [15, 16]])
e = torch.tensor([[17, 18], [19, 20]])
torch.tensordot(a, b, dims=2, out=None)
torch.tensordot(a, b, dims=1, out=None)
torch.tensordot(a, b, dims=0, out=None)