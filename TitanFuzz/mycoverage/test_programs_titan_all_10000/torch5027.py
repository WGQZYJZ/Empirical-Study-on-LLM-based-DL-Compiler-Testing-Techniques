import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.ones(2, 3)
torch.Tensor.normal_(input_tensor, mean=0, std=1)