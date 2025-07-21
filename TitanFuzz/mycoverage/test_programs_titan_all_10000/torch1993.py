import torch
from torch import nn
from torch.autograd import Variable
t1 = torch.randn(3, 5)
t2 = torch.randn(3, 5)
t3 = torch.hstack((t1, t2))
t4 = torch.randn(3, 2)
t5 = torch.randn(3, 2)
t6 = torch.randn(3, 2)
t7 = torch.randn(3, 2)
t8 = torch.hstack((t4, t5, t6, t7))