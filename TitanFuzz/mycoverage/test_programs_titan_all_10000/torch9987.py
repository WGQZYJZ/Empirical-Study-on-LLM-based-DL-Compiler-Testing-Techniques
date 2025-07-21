import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 5)
torch.Tensor.multiply_(input_tensor, 2)