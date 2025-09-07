import torch
from torch import nn
from torch.autograd import Variable

data = torch.rand(3, 3)
result = torch.exp2(data)