import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3, 4)
torch.Tensor.renorm(input_tensor, p=2, dim=1, maxnorm=2)