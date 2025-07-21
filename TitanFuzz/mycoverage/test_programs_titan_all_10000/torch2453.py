import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[True, True, False], [False, True, False], [True, False, False], [False, False, True]])
_output_tensor = torch.Tensor.logical_not(_input_tensor)