import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
index = torch.tensor([0, 2, 3])
tensor = torch.randn(2, 3, 4, 5)
torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)