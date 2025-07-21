import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 3, 3)
output_tensor = torch.Tensor.narrow(input_tensor, 1, 0, 2)
output_tensor = torch.Tensor.narrow(input_tensor, 2, 0, 2)