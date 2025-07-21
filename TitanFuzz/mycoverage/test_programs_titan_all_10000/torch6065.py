import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn((2, 3), dtype=torch.float32, requires_grad=True)
output = torch.special.logit(input, eps=1e-12)