import torch
from torch import nn
from torch.autograd import Variable
start = 1
end = 10
steps = 5
result = torch.logspace(start, end, steps)
out = torch.zeros(steps)
result = torch.logspace(start, end, steps, out=out)