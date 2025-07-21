import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
torch.Tensor.tanh_(input_tensor)