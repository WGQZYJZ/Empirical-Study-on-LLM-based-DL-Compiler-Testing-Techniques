import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([[1, (- 1), 0], [2, 3, 4]])
y = torch.nn.functional.tanh(x)
x = torch.tensor([[1, (- 1), 0], [2, 3, 4]])
y = torch.nn.functional.tanh(x)
x = torch.tensor([[1, (- 1), 0], [2, 3, 4]])
y = torch.nn.functional.tanh(x)