'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.scatter\ntorch.scatter(input, dim, index, src)\n'
import torch
input = torch.randn(2, 3)
torch.scatter(input, 0, torch.tensor([[0, 1, 0], [1, 0, 0]]), 1)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, out=None)\n'
import torch
input = torch.randn(2, 3)
torch.gather(input, 0, torch.tensor([[0, 1, 0], [1, 0, 0]]))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, out=None)\n'
import torch
input = torch.randn(2, 3)