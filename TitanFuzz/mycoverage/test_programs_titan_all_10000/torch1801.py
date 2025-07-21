import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([6, 8, 10], dtype=torch.int32)
y = torch.tensor([2, 4, 6], dtype=torch.int32)
torch.lcm(x, y)
out = torch.empty(3, dtype=torch.int32)
torch.lcm(x, y, out=out)
out