import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
strided_data = torch.empty_strided(size=[1, 2, 3], stride=[3, 1, 1])