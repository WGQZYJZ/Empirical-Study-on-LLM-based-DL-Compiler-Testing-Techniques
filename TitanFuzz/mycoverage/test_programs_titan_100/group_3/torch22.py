import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 3)
output_data = torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)