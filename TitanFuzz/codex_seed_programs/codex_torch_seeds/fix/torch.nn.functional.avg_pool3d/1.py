'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 3, 3, 3))
output = nn.functional.avg_pool3d(input, kernel_size=2, stride=2, padding=0)
print(output)
output = nn.functional.avg_pool3d(input, kernel_size=2, stride=2, padding=1)
print(output)