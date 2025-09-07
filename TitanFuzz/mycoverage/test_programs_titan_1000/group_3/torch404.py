import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(4, 4)
data_rolled = torch.roll(data, shifts=1, dims=1)