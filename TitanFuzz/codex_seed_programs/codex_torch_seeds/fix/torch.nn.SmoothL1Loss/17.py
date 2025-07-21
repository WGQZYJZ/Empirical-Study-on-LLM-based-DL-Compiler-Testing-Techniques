"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
import torch.nn as nn
N = 64
D_in = 1000
H = 100
D_out = 10
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
loss_fn = nn.SmoothL1Loss(reduction='sum')
y_pred = torch.randn(N, D_out)
loss = loss_fn(y_pred, y)
print(loss)