import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 2)
torch.Tensor.sgn_(input_tensor)