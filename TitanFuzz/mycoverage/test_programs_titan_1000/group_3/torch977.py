import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
target = torch.LongTensor([0, 2, 1])
loss = torch.nn.functional.nll_loss(input, target)