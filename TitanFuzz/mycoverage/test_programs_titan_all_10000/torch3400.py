import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 3, dtype=torch.float)
(u, s, v) = torch.svd(input)