import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[10, 20, 30], [40, 50, 60]])
output_tensor = torch.Tensor.subtract(input_tensor, other)
output_tensor = torch.Tensor.subtract(input_tensor, other, alpha=0.5)
output_tensor = torch.Tensor.subtract(input_tensor, other, alpha=2)