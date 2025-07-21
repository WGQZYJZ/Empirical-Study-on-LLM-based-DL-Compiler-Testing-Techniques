"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
x = torch.randn(1, 1, requires_grad=True)
y = torch.randn(1, 1, requires_grad=True)
loss = torch.nn.MSELoss()
print(loss(x, y))