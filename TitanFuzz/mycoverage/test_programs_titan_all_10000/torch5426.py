import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 3)
output_tensor = torch.Tensor.narrow_copy(input_tensor, 0, 1, 3)