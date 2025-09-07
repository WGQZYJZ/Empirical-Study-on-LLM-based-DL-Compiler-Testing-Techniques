import torch
from torch import nn
from torch.autograd import Variable

input_data = Variable(torch.randn(1, 5))
log_sigmoid = torch.nn.LogSigmoid()