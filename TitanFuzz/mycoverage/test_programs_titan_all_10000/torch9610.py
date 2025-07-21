import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[2, 4, 6], [8, 10, 12]])
output_tensor = torch.Tensor.floor_divide(input_tensor, 2)