import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)
loss_fn = torch.nn.MSELoss(size_average=False)
model = torch.nn.Linear(D_in, H)
model2 = torch.nn.Linear(H, D_out)
model = torch.nn.Sequential(model, model2)