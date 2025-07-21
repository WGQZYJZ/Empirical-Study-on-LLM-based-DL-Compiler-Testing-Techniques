import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
torch.Tensor.clip_(input_tensor, min=0.4, max=0.6)