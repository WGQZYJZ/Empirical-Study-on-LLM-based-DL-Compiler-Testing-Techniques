import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, dtype=torch.float32)
buffer = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)