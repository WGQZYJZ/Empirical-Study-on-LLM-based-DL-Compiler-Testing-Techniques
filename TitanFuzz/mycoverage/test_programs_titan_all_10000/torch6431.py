import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([1.0, 2.0, 3.0])
_output_tensor = torch.Tensor.log1p_(_input_tensor)