import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.select(input_tensor, 0, 0)
output_tensor = torch.Tensor.select(input_tensor, 0, 1)
output_tensor = torch.Tensor.select(input_tensor, 1, 0)
output_tensor = torch.Tensor.select(input_tensor, 1, 1)
output_tensor = torch.Tensor.select(input_tensor, 1, 2)