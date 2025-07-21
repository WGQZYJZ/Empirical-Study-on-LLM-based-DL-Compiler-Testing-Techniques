import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(1, 11)
torch.Tensor.geometric_(data, 0.5)