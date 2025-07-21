"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
loss = torch.nn.functional.mse_loss(x, y)
print(loss)