import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 224, 224)
arcsinh_out = torch.Tensor.arcsinh(input_tensor)