import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
torch.Tensor.sign_(input_tensor)
input_tensor = torch.randn(4, 4)
torch.Tensor.sin_(input_tensor)