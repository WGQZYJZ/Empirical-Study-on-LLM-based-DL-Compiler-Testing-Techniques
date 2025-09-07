import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.tensor([[True, False], [True, True]])
_output_tensor = torch.Tensor.all(_input_tensor, dim=None, keepdim=False)