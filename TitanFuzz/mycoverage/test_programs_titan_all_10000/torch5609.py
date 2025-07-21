import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 4, 5)
output_tensor = torch.Tensor.unsqueeze_(input_tensor, dim=0)