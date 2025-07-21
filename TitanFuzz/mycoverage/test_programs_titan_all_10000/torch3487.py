import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
torch.Tensor.fill_diagonal_(input_tensor, fill_value=10, wrap=False)