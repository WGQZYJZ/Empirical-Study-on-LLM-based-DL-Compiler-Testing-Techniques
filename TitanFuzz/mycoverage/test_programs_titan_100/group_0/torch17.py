import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3, 4, 5)
digamma_result = torch.Tensor.digamma_(input_tensor)