import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([10, 2, 3, 4])
other = torch.tensor([2, 3, 4, 5])
torch.Tensor.lcm(input_tensor, other)