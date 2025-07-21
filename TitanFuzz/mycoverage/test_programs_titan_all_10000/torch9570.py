import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[float('nan'), float('-inf'), float('inf')], [float('nan'), float('-inf'), float('inf')], [float('nan'), float('-inf'), float('inf')]])
output_tensor = torch.Tensor.nan_to_num(input_tensor, nan=0.0, posinf=None, neginf=None)