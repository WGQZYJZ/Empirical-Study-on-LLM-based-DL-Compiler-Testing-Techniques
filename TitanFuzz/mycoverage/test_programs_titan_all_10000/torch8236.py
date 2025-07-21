import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[10.0, 10.0, 10.0, 10.0, 10.0], [1.0, 2.0, 3.0, 4.0, 5.0]])
output = torch.multinomial(input, 3)