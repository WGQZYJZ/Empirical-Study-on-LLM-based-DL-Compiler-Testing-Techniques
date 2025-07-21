import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
tensor2 = torch.tensor([1, 1])
torch.Tensor.index_add(input_tensor, 0, index, tensor2)