'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eye\ntorch.eye(n, m=None, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
inp = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
out = torch.eye(inp.shape[1], inp.shape[0])
print(out)