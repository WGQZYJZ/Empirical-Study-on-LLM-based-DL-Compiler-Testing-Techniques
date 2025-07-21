import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.index_fill_(input_tensor, 1, torch.tensor([0, 2]), 0)