import torch
from torch import nn
from torch.autograd import Variable
t1 = torch.rand(3, 3)
t2 = torch.rand(3, 3)
t3 = torch.rand(3, 3)
t4 = torch.rand(3, 3)
t5 = torch.rand(3, 3)
t_stack = torch.row_stack((t1, t2, t3, t4, t5))