import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1.0, 0.0, 0.0], [0.0, float('nan'), float('inf')], [float('-inf'), float('inf'), float('nan')]])
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)