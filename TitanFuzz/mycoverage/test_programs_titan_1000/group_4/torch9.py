import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
torch.Tensor.remainder_(input_tensor, 2)