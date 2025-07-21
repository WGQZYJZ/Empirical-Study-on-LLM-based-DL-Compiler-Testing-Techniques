import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([(- 1), 0, 1])
output = torch.nn.functional.sigmoid(input)
input = torch.Tensor([(- 1), 0, 1])
output = torch.nn.functional.tanh(input)