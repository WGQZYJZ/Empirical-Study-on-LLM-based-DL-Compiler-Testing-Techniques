import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(4, 4)
torch.nn.init.sparse_(data, sparsity=0.5, std=0.01)