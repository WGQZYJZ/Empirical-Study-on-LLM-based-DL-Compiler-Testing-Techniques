import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
torch.Tensor.cauchy_(input_tensor, median=0, sigma=1, generator=None)