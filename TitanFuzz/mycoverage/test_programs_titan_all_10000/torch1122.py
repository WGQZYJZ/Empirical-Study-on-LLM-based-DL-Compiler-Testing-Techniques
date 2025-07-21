import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(20, 20)
torch.Tensor.polygamma_(input_tensor, n=1)