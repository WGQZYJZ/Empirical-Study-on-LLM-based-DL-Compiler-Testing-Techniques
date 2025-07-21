import torch
from torch import nn
from torch.autograd import Variable
torch.Tensor.detach_(torch.randn(2, 3, 4))