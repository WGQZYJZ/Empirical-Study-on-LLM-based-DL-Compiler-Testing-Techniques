import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.Tensor.renorm_(input_tensor, p=2, dim=0, maxnorm=1)