import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3, 4)
other = torch.rand(2, 3, 4)
zeta = torch.special.zeta(input, other)
zeta = torch.special.zeta(input, other, out=None)
zeta = torch.special.zeta(input, other, out=torch.empty(2, 3, 4))
zeta = torch.special.zeta