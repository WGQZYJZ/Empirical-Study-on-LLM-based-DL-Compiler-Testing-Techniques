'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
from torch.autograd import Variable
import torch.nn.functional as F
input = Variable(torch.randn(1, 1, 4, 4))
output = F.avg_pool2d(input, kernel_size=2, stride=2)
print(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch