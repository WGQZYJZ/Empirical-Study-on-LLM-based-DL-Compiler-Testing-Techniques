import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand((4, 4))
torch.Tensor.clip_(input_tensor, min=0.5, max=0.7)