import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 5)
p = 2
dim = 0
maxnorm = 2
output_tensor = torch.Tensor.renorm_(input_tensor, p, dim, maxnorm)