import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
input_tensor[(0, 0)] = float('nan')
input_tensor[(0, 1)] = float('inf')
input_tensor[(0, 2)] = float('-inf')
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)