import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.Tensor([[1, 2], [3, 4]])
torch.Tensor.renorm(input_tensor, 1, 0, 5)