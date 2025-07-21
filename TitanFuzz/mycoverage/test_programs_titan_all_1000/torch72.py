import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.randn(3, 4))
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False)