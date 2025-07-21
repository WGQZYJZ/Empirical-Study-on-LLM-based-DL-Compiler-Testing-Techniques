import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
torch.Tensor.cauchy_(input_tensor, median=0, sigma=1)