import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
new_tensor = torch.Tensor.new_tensor(input_tensor, data=None, dtype=None, device=None, requires_grad=False)