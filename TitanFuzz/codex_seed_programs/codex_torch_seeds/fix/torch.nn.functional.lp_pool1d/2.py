'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_size = (1, 3, 3)
input_data = Variable(torch.randn(input_size))
norm_type = 2
kernel_size = 2
stride = None
ceil_mode = False
output = torch.nn.functional.lp_pool1d(input_data, norm_type, kernel_size, stride, ceil_mode)
print('output: ', output)