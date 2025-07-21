import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1.0, 2.0, 3.0])
torch.Tensor.cosh_(input_tensor)