import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(1, 3, 3)
random_tensor = torch.Tensor.random_(input_tensor, from_=1, to=10)