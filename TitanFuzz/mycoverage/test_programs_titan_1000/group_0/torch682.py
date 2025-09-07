import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.ones(2, 3)
torch.Tensor.diagflat(input_tensor, offset=0)