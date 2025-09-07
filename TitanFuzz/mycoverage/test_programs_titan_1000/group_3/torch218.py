import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 3)
strided_data = torch.empty_strided(size=(2, 3, 3), stride=(1, 2, 1))