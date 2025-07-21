"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 10), requires_grad=True)
y = Variable(torch.randn(1, 10), requires_grad=True)
loss = torch.nn.functional.mse_loss(x, y)
print(loss)
loss.backward()
print(x.grad)
print(y.grad)