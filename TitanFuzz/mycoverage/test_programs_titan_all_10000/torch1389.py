import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor(3, 5)
torch.Tensor.random_(input_tensor, from_=0, to=None, generator=None)