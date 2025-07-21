import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]))
padding = 2
replicationPad1d = torch.nn.ReplicationPad1d(padding)
output = replicationPad1d(input)