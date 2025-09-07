import torch
from torch import nn
from torch.autograd import Variable

input_tensor = Variable(torch.randn(1, 3))
output_tensor = torch.Tensor.arccos(input_tensor)