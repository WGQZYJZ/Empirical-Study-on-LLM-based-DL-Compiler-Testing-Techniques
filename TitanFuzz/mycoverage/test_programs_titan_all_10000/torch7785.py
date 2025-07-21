import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
output_tensor = torch.Tensor.corrcoef(input_tensor)