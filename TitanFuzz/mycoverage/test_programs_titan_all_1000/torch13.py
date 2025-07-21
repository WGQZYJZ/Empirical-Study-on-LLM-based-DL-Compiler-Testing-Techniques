import torch
from torch import nn
from torch.autograd import Variable
start = 0
end = 10
steps = 5
base = 2
torch.logspace(start, end, steps, base=base)