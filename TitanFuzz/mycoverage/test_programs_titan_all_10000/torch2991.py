import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
target = torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
loss = torch.nn.functional.mse_loss(input, target)