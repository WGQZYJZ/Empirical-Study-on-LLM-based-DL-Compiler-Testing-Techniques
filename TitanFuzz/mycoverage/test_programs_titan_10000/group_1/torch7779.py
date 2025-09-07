import torch
from torch import nn
from torch.autograd import Variable

input = torch.tensor([(- 1), 1, 1, (- 1), 1, (- 1), 1, (- 1)], dtype=torch.float)
other = torch.tensor([1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1)], dtype=torch.float)
output = torch.copysign(input, other)