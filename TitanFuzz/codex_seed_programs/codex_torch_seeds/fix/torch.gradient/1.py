'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gradient\ntorch.gradient(input, *, spacing=1, dim=None, edge_order=1)\n'
import torch
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], requires_grad=True)
torch.gradient(x, dim=0)
torch.gradient(x, dim=1)
torch.gradient(x, dim=1, edge_order=2)