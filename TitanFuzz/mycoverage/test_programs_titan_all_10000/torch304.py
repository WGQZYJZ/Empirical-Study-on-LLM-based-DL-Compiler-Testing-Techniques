import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
_input_tensor[0][0] = float('nan')
_input_tensor[0][1] = float('inf')
_input_tensor[0][2] = float('-inf')
_output_tensor = torch.Tensor.nan_to_num_(_input_tensor)