import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5)
unfold = torch.nn.Unfold(kernel_size=2, dilation=1, padding=0, stride=1)
output_data = unfold(input_data)