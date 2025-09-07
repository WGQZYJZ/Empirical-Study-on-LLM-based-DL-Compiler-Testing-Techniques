import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(5, 3)
torch.Tensor.tan_(input_tensor)