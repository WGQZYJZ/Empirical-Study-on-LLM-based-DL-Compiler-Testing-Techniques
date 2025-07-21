import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 1, 2], [2, 3, 4]])
torch.Tensor.gt_(input_tensor, 2)