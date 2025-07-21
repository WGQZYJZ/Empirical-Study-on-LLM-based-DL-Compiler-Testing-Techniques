'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2], [3, 4], [5, 6]])
torch.kron(input, other)
torch.kron(input, other, out=torch.FloatTensor())