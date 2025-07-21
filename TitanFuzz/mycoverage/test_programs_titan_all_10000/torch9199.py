import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
other = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
torch.Tensor.igammac_(input_tensor, other)