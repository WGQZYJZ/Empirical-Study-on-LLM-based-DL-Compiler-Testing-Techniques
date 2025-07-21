import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
mask = torch.tensor([[True, True, False, False], [False, False, True, True], [True, False, False, True]])
tensor = torch.tensor([[10, 20], [30, 40], [50, 60]])
torch.Tensor.masked_scatter(input_tensor, mask, tensor)