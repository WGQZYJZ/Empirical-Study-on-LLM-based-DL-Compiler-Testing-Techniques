import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_tensor = torch.tensor([[10, 20, 30], [40, 50, 60]])
torch.Tensor.lcm_(input_tensor, other_tensor)