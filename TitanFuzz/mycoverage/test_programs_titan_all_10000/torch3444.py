import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
torch.Tensor.index_fill_(input_tensor, 0, torch.tensor([0, 2]), 100)