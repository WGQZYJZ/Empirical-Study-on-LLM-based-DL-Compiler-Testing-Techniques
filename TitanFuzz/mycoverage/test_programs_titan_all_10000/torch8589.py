import torch
from torch import nn
from torch.autograd import Variable
t1 = torch.randn(2, 4)
t2 = torch.randn(2, 4)
t3 = torch.hstack((t1, t2))