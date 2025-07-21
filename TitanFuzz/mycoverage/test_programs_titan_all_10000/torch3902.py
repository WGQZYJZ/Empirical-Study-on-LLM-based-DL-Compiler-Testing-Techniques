import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1, 2, 3])
other = torch.tensor([1, 2, 3])
torch.Tensor.igamma_(input_tensor, other)