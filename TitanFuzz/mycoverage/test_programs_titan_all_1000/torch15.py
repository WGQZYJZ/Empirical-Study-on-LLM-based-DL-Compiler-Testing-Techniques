import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
other_tensor = torch.rand(4, 5)
torch.Tensor.dot(input_tensor, other_tensor)