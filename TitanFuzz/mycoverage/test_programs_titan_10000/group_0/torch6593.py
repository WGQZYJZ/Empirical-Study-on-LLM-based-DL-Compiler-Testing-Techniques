import torch
from torch import nn
from torch.autograd import Variable

input_tensor = Variable(torch.randn(2, 3, 3))
logdet_output = torch.Tensor.logdet(input_tensor)