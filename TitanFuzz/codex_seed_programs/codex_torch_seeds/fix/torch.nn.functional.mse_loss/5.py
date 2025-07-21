"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
x = torch.rand(10)
y = torch.rand(10)
print('x: ', x)
print('y: ', y)
loss = F.mse_loss(x, y)
print('loss: ', loss)