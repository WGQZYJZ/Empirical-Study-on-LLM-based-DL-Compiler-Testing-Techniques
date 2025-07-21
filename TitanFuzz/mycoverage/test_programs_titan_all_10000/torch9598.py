import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, requires_grad=True)
torch.Tensor.retains_grad(input_tensor, True)