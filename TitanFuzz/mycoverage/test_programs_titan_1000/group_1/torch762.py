import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3, 3)
output = torch.nn.functional.avg_pool3d(input_data, kernel_size=1, stride=1, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)