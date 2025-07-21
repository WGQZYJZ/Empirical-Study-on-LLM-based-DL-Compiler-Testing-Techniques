'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool2d\ntorch.nn.MaxUnpool2d(kernel_size, stride=None, padding=0)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, H, W) = (2, 3, 4, 4)
x = Variable(torch.randn(N, C, H, W).type(dtype), requires_grad=True)
indices = Variable(torch.LongTensor([0, 2, 2, 2, 1, 1, 1, 1]).view(2, 2, 2))
pool = torch.nn.MaxPool2d(2, stride=2, return_indices=True)
unpool = torch.nn.MaxUnpool2d(2, stride=2)
(y, indices) = pool(x)
x_hat = unpool(y, indices)
print(x)
print(y)
print(x_hat)