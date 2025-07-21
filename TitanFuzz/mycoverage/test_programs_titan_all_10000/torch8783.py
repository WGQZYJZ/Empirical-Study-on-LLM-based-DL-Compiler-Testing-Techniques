import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
torch.Tensor.index_copy_(input_tensor, 0, torch.tensor([1, 2]), torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))