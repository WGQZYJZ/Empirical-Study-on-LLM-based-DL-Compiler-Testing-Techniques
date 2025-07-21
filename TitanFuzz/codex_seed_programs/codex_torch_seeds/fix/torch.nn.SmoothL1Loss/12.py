"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
import torch
x = torch.rand(10000)
y = ((1.5 * x) + 3)
loss_fn = torch.nn.SmoothL1Loss()
loss = loss_fn(y, x)
print(loss)