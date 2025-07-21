import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[float('nan'), float('-inf'), float('inf')], [1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
nan_to_num_input = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)