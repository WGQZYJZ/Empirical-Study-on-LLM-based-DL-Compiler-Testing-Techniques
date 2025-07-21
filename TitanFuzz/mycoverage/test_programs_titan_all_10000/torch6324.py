import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=torch.bool)
tensor = torch.randn(5, 3)
torch.Tensor.masked_scatter(input_tensor, mask, tensor)