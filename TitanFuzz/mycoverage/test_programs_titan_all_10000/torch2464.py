import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], requires_grad=True)
target = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], requires_grad=True)
loss = torch.nn.functional.binary_cross_entropy(input, target)