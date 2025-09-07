import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.ones(1, 1, 4, 4))
pad = torch.nn.ReplicationPad2d(2)
output = pad(input)