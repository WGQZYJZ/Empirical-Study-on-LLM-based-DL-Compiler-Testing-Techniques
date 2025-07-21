import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 2, 3, 4)
output_tensor = torch.Tensor.true_divide(input_tensor, 2)