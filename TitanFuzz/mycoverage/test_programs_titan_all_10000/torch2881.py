import torch
from torch import nn
from torch.autograd import Variable
input1 = Variable(torch.randn(3, 5))
input2 = Variable(torch.randn(3, 5))
input3 = Variable(torch.randn(3, 5))
loss = torch.nn.TripletMarginWithDistanceLoss()
output = loss(input1, input2, input3)