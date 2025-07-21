'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool2d\ntorch.nn.functional.lp_pool2d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn as nn
from torch.nn.functional import lp_pool2d
from torch.autograd import Variable
import torch
input_data = Variable(torch.rand(1, 1, 5, 5))
output_data = lp_pool2d(input_data, norm_type=2, kernel_size=3, stride=2)
print(output_data)