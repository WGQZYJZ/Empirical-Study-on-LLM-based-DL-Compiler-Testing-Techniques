import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(10, 2)
torch.Tensor.renorm_(input_tensor, 1, 0, 10)