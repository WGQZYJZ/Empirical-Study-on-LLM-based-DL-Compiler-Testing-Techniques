import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
output = torch.less_equal(input_data, 0.5)