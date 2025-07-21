import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
divisor = torch.tensor([2, 2, 2, 2])
output = torch.true_divide(input_data, divisor)