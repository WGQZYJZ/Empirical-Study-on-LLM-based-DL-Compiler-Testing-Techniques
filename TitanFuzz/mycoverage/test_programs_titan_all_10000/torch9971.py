import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
torch.Tensor.cauchy_(input_tensor, median=2, sigma=1)