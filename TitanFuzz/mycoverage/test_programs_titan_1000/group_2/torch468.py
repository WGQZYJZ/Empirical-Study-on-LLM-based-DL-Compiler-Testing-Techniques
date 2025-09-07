import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.select(input_tensor, 0, 0)
output_tensor = torch.Tensor.select(input_tensor, 0, 1)
output_tensor = torch.Tensor.select(input_tensor, 1, 0)
output_tensor = torch.Tensor.select(input_tensor, 1, 1)
output_tensor = torch.Tensor.select(input_tensor, 1, 2)