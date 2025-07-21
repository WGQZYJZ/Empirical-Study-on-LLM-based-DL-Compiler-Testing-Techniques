import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3, 5)
torch.Tensor.sin_(input_tensor)