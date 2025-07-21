import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.ones(2, 3)
value = 2
torch.Tensor.multiply_(input_tensor, value)