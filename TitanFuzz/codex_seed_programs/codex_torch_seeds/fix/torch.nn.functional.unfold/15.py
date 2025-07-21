'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.unfold\ntorch.nn.functional.unfold(input, kernel_size, dilation=1, padding=0, stride=1)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, H, W) = (2, 3, 4, 5)
x = Variable(torch.randn(N, C, H, W).type(dtype), requires_grad=True)
kernel_size = 2
dilation = 1
padding = 1
stride = 1
y = torch.nn.functional.unfold(x, kernel_size, dilation, padding, stride)
print(y.size())
print(y)