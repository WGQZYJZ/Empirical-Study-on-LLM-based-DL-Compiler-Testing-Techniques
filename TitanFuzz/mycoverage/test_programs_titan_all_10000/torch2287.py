import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4, 5)
torch.Tensor.logcumsumexp(input_tensor, dim=1)