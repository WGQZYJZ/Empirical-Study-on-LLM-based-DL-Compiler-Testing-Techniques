import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.repeat_interleave(input_tensor, repeats=3, dim=0)