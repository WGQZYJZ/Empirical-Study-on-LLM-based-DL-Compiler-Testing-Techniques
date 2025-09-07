import torch
from torch import nn
from torch.autograd import Variable
tensor_a = torch.rand(3, 3)
tensor_b = torch.rand(3, 3)
tensor_c = torch.renorm(tensor_a, p=2, dim=0, maxnorm=1)
tensor_d = torch.renorm(tensor_b, p=2, dim=1, maxnorm=1)