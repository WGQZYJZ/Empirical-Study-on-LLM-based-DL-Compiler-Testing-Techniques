import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 10))
target_data = Variable(torch.randn(5, 10))
loss_fn = torch.nn.KLDivLoss()
loss = loss_fn(input_data, target_data)