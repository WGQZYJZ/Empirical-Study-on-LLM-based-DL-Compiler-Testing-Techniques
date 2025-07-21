import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 1, 28, 28)
torch.Tensor.fix_(input_tensor)