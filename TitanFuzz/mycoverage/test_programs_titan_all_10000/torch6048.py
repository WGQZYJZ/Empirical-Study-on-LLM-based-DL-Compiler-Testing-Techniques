import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4, requires_grad=True)
other_data = torch.randn(4, 4, requires_grad=True)
output_data = torch.minimum(input_data, other_data)