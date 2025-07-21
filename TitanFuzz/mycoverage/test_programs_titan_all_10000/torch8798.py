import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(5, 3, requires_grad=True)
result = torch.nn.PairwiseDistance()(data, data)