import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
output_data = torch.Tensor.arcsinh(input_data)