import torch
from torch import nn
from torch.autograd import Variable

input = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
output = torch.bitwise_not(input)