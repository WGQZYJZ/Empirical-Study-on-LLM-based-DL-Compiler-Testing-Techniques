import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.randn(3, 5)
tensor = torch.renorm(tensor, p=2, dim=1, maxnorm=1)