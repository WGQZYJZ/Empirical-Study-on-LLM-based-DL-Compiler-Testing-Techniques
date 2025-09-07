import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.kthvalue(input_tensor, 1, dim=1, keepdim=False)