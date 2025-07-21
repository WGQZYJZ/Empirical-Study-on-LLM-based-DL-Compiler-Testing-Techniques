import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
swapdims_tensor = torch.Tensor.swapdims(input_tensor, 0, 2)