import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
output_tensor = torch.Tensor.geometric_(input_tensor, 0.5, generator=None)