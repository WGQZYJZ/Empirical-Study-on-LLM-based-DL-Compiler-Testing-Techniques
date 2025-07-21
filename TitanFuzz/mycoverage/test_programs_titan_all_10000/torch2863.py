import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
torch.Tensor.tril_(input_tensor, diagonal=0)