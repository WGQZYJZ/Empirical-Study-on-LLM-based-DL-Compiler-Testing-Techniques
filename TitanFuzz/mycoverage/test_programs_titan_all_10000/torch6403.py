import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
target = torch.Tensor([[0, 0, 1], [0, 0, 1]])
loss = torch.nn.functional.soft_margin_loss(input, target)