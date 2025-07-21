import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(1, 7).reshape(2, 3)
diag = torch.diag(input)