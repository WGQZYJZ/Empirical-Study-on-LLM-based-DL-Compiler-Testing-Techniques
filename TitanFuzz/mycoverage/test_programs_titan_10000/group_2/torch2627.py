import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(1, 2, 3, 3)
hardswish = torch.nn.Hardswish()
output = hardswish(input_data)