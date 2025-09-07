import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(4, 10))
target_data = Variable(torch.randn(4, 10))
loss = torch.nn.functional.mse_loss(input_data, target_data)