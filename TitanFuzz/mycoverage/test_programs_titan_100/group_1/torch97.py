import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.normal_(input_tensor, mean=0, std=1)