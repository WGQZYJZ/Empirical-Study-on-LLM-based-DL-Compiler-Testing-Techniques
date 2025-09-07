import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3, 3)
output_data = torch.Tensor.resolve_conj(input_data)