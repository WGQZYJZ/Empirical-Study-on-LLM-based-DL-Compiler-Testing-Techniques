import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(0, 10, (3, 3), dtype=torch.float32)
output = torch.empty_like(input)