import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
conj_input_data = torch.Tensor.conj(input_data)