import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([3, 4, 6, 8])
other = torch.tensor([2, 3, 4, 5])
torch.Tensor.lcm_(input_tensor, other)