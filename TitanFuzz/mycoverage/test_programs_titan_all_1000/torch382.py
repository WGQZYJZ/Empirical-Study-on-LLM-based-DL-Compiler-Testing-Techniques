import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
y = torch.index_select(x, 0, torch.LongTensor([0, 2]))