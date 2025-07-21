import torch
from torch import nn
from torch.autograd import Variable
data = torch.ones(2, 3, 4)
result = torch.ravel(data)