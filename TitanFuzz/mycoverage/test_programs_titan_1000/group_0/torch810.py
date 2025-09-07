import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
output_tensor = torch.Tensor.diag(input_tensor, diagonal=0)
output_tensor = torch.diag(input_tensor, diagonal=0)