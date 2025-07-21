import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
torch.Tensor.renorm_(input_tensor, 1, 0, 2)
torch.Tensor.renorm_(input_tensor, 1, 1, 2)
torch.Tensor.renorm_(input_tensor, 2, 1, 2)
torch.Tensor.renorm_(input_tensor, 2, 0, 2)