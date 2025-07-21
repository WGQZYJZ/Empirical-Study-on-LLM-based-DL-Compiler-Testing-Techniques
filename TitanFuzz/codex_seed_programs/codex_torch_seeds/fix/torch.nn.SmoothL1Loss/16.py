"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
import torch.nn as nn
x = torch.tensor([[0.5, 0.5]], requires_grad=True)
y = torch.tensor([[1.0, 1.0]], requires_grad=True)
loss_fn = nn.SmoothL1Loss()
loss = loss_fn(x, y)
print(loss)
loss.backward()
print(x.grad)
print(y.grad)