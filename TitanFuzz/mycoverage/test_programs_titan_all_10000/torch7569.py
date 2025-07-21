import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor(2, 3)
result = torch.Tensor.random_(input_tensor, from_=0, to=1, generator=None)
input_tensor = torch.Tensor(2, 3)