import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 4)
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=2, padding=0, dilation=1, return_indices=False, ceil_mode=False)