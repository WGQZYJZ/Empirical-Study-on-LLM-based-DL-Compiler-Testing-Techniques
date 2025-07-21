import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(4, 4)
data_frexp = torch.frexp(data)