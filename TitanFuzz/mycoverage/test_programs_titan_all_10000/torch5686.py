import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
result = torch.Tensor.is_complex(_input_tensor)