import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
result = torch.Tensor.renorm(input_tensor, p=2, dim=0, maxnorm=1)
result = torch.Tensor.renorm(input_tensor, p=2, dim=1, maxnorm=1)