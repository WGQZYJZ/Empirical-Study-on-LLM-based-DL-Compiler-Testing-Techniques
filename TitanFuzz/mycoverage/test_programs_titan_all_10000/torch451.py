import torch
from torch import nn
from torch.autograd import Variable
t1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
t2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
t3 = torch.vstack((t1, t2))
t4 = torch.tensor([[13, 14, 15], [16, 17, 18]])
t5 = torch.tensor([[19, 20, 21], [22, 23, 24]])
t6 = torch.cat((t4, t5), dim=0)
t7 = torch.cat((t4, t5), dim=1)
t8 = torch.cat((t4, t5))