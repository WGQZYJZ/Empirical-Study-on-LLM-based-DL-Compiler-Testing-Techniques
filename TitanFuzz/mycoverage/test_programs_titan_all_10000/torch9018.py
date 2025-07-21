import torch
from torch import nn
from torch.autograd import Variable
start = 0.1
end = 1.0
steps = 10
data = torch.linspace(start, end, steps)