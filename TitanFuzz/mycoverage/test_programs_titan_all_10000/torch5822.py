import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 4)
torch.Tensor.sort(_input_tensor, dim=(- 1), descending=False)
_input_tensor = torch.randn(3, 4)
torch.Tensor.sort(_input_tensor, dim=(- 1), descending=True)