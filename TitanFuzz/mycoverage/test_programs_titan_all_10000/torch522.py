import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
torch.Tensor.roll(_input_tensor, shifts=1, dims=1)