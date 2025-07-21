import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(5, 3, 5, 5)
torch.Tensor.resolve_neg(_input_tensor)