import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(1, 9).view(2, 2, 2)
result = torch.fliplr(data)