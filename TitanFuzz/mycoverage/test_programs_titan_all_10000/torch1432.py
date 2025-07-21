import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
torch.Tensor.renorm_(input_tensor, 2, 0, 5)