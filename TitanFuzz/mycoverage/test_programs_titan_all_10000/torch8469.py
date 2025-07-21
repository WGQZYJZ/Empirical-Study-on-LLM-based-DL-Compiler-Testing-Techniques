import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 5)
output = torch.logaddexp(input_data, input_data)