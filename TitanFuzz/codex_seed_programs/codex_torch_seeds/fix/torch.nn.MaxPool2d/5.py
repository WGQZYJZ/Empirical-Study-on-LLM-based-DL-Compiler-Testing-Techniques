'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, H, W) = (1, 2, 3, 3)
x = Variable(torch.randn(N, C, H, W).type(dtype), requires_grad=False)
max_pool = torch.nn.MaxPool2d(2, stride=2)
y = max_pool(x)
print(x)
print(y)