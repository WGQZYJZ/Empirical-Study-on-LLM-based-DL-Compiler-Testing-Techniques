import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
torch.Tensor.sort(_input_tensor, dim=(- 1), descending=False)