'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
input = Variable(torch.randn(1, 3, 10, 10, 10))
output = torch.nn.functional.avg_pool3d(input, kernel_size=3, stride=2)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool3d\ntorch.nn.functional.max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
input = Variable(torch.randn(1, 3, 10, 10, 10))
output = torch.nn.functional.max_pool3d(input, kernel_size=3, stride=2)