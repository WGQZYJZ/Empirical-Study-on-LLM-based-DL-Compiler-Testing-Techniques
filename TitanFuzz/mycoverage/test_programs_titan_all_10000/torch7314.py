import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1.0, float('nan'), float('inf')], [float('-inf'), 2.0, float('nan')]], dtype=torch.float32)
_nan_to_num_output = torch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)