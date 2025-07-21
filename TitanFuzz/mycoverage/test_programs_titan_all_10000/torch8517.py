import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.conj_physical(_input_tensor)