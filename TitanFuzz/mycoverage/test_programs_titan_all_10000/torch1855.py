import torch
from torch import nn
from torch.autograd import Variable
start = 0.0
end = 1.0
steps = 5
result = torch.linspace(start, end, steps)