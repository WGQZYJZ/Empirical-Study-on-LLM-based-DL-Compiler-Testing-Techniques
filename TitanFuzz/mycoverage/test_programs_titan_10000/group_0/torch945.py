import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(3, 3)
result_tensor = torch.Tensor.inverse(input_tensor)
input_tensor = torch.rand(3, 3)
result_tensor = torch.Tensor.mm(input_tensor, input_tensor)
input_tensor = torch.rand(3, 3)
result_tensor = torch.Tensor.mul(input_tensor, input_tensor)