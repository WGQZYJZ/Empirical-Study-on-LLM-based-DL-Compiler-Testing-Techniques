import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([(1 + 1j), (2 + 2j), (3 + 3j), (4 + 4j)])
output = torch.imag(input)