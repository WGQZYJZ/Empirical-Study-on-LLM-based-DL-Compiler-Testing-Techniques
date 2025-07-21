import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([(- 5), (- 4), (- 3), (- 2), (- 1), 0, 1, 2, 3, 4, 5])
output = torch.special.i0e(input)