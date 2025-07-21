import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
torch.Tensor.index_fill_(input_tensor, 0, torch.tensor([0, 2]), 1)
input_tensor = torch.randn(3, 3)
torch