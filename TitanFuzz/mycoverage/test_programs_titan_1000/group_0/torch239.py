import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
torch.Tensor.dist(input_tensor, other_tensor, p=2)