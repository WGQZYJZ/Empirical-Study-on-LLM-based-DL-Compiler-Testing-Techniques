import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.char(input_data)