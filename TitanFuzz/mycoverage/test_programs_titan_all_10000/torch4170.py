import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.Tensor.map_(input_tensor, (lambda x: (x + 1)))