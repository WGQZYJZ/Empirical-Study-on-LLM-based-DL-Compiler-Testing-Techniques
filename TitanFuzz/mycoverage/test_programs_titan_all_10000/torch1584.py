import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[float('NaN'), (- float('inf')), float('inf')], [1, 2, 3], [0, 1, 1]])
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)