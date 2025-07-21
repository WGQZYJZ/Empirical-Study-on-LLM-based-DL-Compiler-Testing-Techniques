import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 3, 3, 2)
data_conj = torch.conj_physical(data)