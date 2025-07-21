import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 5)
result = torch.renorm(input_data, p=2, dim=0, maxnorm=1)