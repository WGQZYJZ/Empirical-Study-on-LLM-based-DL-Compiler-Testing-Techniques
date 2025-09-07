import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(1, 6)
torch.Tensor.sub_(input_tensor, other=torch.ones(5))