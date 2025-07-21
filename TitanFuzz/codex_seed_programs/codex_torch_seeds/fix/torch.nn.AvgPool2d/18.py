'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5, 5))
pool = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)
print(pool(input))