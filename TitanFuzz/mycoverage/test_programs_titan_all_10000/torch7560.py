import torch
from torch import nn
from torch.autograd import Variable
a = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
b = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
torch.bitwise_and(a, b)