import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.ones(2, 2)
torch.Tensor.random_(input_tensor, from_=0, to=None, generator=None)
input_tensor = torch.ones(2, 2)