import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 10, dtype=torch.float32)
input_tensor[3] = float('nan')
input_tensor[5] = float('inf')
input_tensor[7] = float('-inf')
result = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)