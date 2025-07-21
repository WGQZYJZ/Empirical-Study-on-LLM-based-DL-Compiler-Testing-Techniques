import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False)