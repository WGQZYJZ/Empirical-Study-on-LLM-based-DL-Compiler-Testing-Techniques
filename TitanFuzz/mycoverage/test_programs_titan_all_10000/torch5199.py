import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.arange(start=0, end=9, step=1)
_output_tensor = torch.Tensor.square(_input_tensor)