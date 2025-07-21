import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
result = torch.Tensor.isclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)