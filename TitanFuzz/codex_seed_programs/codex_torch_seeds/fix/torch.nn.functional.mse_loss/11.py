"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(1, 1))
target = Variable(torch.randn(1, 1))
loss = torch.nn.functional.mse_loss(input, target)
print(loss)
'\nExpected output:\n1.3835\n'