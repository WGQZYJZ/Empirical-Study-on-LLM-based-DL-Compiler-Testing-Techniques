import torch
from torch import nn
from torch.autograd import Variable
data = torch.randint(0, 2, (4, 4), dtype=torch.int8)
result = torch.bitwise_and(data, torch.ones((4, 4), dtype=torch.int8))