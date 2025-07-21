'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmin\ntorch.fmin(input, other, *, out=None)\n'
import torch
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], requires_grad=True)
y = torch.tensor([[10.0, 20.0, 30.0], [40.0, 50.0, 60.0]], requires_grad=True)
torch.fmin(x, y)