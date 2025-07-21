import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.Tensor.allclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)