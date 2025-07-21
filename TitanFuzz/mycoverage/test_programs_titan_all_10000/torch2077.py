import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 4)
angle_tensor = torch.Tensor.angle(input_tensor)
input_tensor = torch.randn(3, 4)
diag_tensor = torch.Tensor.diag(input_tensor)
input_tensor = torch.randn(3, 4)
trace_tensor = torch.Tensor.trace(input_tensor)