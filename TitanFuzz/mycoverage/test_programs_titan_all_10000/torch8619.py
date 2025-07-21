import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 64, 64)
target = torch.randn(1, 1, 64, 64)
torch.profiler.tensorboard_trace_handler(input, target)