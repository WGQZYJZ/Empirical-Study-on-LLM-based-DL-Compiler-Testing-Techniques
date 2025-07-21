import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
torch.Tensor.index_fill(input_tensor, 0, torch.tensor([0, 2]), (- 100))