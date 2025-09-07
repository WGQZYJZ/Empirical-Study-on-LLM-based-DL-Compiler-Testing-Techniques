import torch
from torch import nn
from torch.autograd import Variable

start = 0
end = 10
steps = 5
result = torch.linspace(start, end, steps)