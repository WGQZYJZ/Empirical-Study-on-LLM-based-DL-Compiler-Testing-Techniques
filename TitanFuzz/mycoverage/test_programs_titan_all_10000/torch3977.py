import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.resolve_neg(_input_tensor)