import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.mv(input, torch.tensor([1.0, 2.0, 3.0]))