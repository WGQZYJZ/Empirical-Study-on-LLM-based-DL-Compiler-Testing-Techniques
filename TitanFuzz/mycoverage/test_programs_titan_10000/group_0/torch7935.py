import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(1, 2, 3, 4)
torch.Tensor.cauchy_(input_tensor)