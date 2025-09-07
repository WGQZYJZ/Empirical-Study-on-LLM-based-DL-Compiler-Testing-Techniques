import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 6)
torch.tensor_split(input, 3, dim=1)