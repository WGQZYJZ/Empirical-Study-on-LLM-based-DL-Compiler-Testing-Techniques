import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]]]))
padding = (0, 0, 1, 2, 3, 4)
replicationPad3d = torch.nn.ReplicationPad3d(padding)
output = replicationPad3d(input)