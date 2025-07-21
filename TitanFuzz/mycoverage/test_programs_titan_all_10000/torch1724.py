import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 5)
output_tensor = torch.Tensor.moveaxis(input_tensor, 0, 1)
output_tensor = torch.Tensor.moveaxis(input_tensor, 1, (- 1))
output_tensor = torch.Tensor.moveaxis(input_tensor, (- 1), 1)