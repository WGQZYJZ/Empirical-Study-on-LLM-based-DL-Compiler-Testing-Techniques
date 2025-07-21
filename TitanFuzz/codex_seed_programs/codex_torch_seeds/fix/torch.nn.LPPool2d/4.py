'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool2d\ntorch.nn.LPPool2d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, H, W) = (2, 3, 4, 4)
a = torch.randn(N, C, H, W).type(dtype)
a = Variable(a, requires_grad=False)
pool = torch.nn.LPPool2d(2, 3, stride=2, ceil_mode=False)
h = pool(a)
print(h)