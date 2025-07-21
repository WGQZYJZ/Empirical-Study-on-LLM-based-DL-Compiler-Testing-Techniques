import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
_mean = torch.Tensor.mean(_input_tensor, dim=1)
_mean = torch.Tensor.mean(_input_tensor, dim=1, keepdim=True)
_mean = torch.Tensor.mean(_input_tensor, dim=0, keepdim=True)