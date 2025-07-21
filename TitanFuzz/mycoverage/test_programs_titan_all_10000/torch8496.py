import torch
from torch import nn
from torch.autograd import Variable
t1 = torch.randn(2, 3)
t2 = torch.randn(4, 3)
t3 = torch.randn(3, 2)
result = torch.block_diag(t1, t2, t3)