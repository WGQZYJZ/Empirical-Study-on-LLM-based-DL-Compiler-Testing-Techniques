import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.log10_(input_tensor)
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.log1p_(input_tensor)