import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 10, (3, 3))
_any_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)