import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1000)
_histc = torch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)