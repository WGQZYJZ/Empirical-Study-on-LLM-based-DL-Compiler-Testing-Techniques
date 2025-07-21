import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 4)
torch.Tensor.msort(_input_tensor)