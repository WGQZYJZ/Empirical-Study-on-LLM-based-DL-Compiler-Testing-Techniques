import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
torch.Tensor.true_divide_(input_tensor, 2)
input_tensor = torch.rand(3, 3)
torch.Tensor.clamp_(input_tensor, min=0.5, max=0.9)
input_tensor = torch.rand(3, 3)