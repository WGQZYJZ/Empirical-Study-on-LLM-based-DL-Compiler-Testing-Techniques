import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(5, 3)
output_tensor = torch.Tensor.sinc(input_tensor)