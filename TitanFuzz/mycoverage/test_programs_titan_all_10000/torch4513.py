import torch
from torch import nn
from torch.autograd import Variable
start = 0
end = 5
steps = 10
result = torch.logspace(start, end, steps)