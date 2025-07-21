import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4, 4)
output_tensor_list = torch.Tensor.dsplit(input_tensor, 2)