import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
index = torch.tensor([[0, 1, 0], [1, 0, 1]], dtype=torch.long)
src = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
output = torch.Tensor.scatter(input_tensor, 0, index, src)