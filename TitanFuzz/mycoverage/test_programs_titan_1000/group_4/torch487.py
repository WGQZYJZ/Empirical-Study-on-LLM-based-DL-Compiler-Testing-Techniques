import torch
from torch import nn
from torch.autograd import Variable
start = 1
end = 5
steps = 10
out = torch.logspace(start, end, steps)