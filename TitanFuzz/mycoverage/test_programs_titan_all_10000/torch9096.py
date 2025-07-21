import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 3, 224, 224)
torch.Tensor.fix_(input)