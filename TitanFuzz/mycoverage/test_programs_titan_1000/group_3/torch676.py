import torch
from torch import nn
from torch.autograd import Variable
input_size = (1, 3, 3)
input_data = Variable(torch.randn(input_size))
norm_type = 2
kernel_size = 2
stride = None
ceil_mode = False
output = torch.nn.functional.lp_pool1d(input_data, norm_type, kernel_size, stride, ceil_mode)