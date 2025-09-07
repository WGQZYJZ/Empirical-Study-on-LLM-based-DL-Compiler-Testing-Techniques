import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(3, 3)
a = (a + a.t())
(e, v) = torch.symeig(a, eigenvectors=True)