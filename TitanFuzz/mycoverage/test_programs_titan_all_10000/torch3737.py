import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, dtype=torch.float32)
other = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
torch.Tensor.igammac_(input_tensor, other)