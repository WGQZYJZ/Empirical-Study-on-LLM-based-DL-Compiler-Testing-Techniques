import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 3, 5], [2, 4, 6]])
output_tensor = torch.Tensor.sort(input_tensor, dim=(- 1), descending=False)