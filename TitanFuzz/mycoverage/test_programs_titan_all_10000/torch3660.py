import torch
from torch import nn
from torch.autograd import Variable
start = 0
end = 10
steps = 5
x = torch.linspace(start, end, steps)
start = 0
end = 10
steps = 5
x = torch.logspace(start, end, steps)
start = 0
end = 10
step = 1
x = torch.arange(start, end, step)