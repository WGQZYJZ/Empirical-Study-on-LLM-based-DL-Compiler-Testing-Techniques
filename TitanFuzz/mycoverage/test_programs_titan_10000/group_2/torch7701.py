import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3, 4)
torch.Tensor.unsqueeze_(input_tensor, dim=0)