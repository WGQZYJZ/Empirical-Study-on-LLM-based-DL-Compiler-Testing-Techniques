import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 4)
output_tensor = torch.Tensor.lerp_(input_tensor, torch.randn(1, 3, 4), 0.5)