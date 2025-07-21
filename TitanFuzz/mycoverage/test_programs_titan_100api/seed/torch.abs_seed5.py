import torch

x = torch.randn(1, 3, requires_grad=True)
y = torch.abs(x)