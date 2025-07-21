'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool2d\ntorch.nn.functional.lp_pool2d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
import torch.nn as nn
import torch.nn.functional as F
input = Variable(torch.randn(1, 1, 5, 5))
output = F.lp_pool2d(input, norm_type=2, kernel_size=2, stride=2)
print(output)