import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 2, 3, 4, 5)
output_tensor = torch.Tensor.resolve_conj(input_tensor)