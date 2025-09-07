import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.randn(3, 3))
output = torch.Tensor.lgamma(input_tensor)