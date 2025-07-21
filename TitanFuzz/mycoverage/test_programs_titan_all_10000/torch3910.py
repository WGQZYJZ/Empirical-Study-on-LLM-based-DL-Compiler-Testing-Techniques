import torch
from torch import nn
from torch.autograd import Variable
start = 0.1
end = 10
steps = 5
out = torch.logspace(start, end, steps)