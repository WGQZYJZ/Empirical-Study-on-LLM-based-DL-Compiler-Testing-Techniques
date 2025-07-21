import torch
x = torch.rand(10000)
y = ((1.5 * x) + 3)
loss_fn = torch.nn.SmoothL1Loss()
loss = loss_fn(y, x)