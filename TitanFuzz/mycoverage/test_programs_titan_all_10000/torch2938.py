import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 3)
a = torch.randn(3, 3)
out = torch.LongTensor()
torch.nonzero(a, out=out)