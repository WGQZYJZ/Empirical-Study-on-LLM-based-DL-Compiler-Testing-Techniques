import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10)
output_tensor = torch.Tensor.log_normal_(input_tensor, mean=1, std=2)