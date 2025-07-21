import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4)
torch.nn.functional.normalize(x, p=2.0, dim=1, eps=1e-12, out=None)