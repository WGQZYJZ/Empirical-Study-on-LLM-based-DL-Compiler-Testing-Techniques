import torch
from torch import nn
from torch.autograd import Variable
a = torch.tensor([[True, True], [False, False]])
b = torch.bitwise_not(a)