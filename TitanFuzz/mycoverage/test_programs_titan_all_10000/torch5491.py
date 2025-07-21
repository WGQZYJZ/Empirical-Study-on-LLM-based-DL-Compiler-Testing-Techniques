import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]])
torch.Tensor.lt_(input_tensor, 2)