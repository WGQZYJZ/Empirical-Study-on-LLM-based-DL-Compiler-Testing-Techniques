'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.optim as optim
dtype = torch.FloatTensor
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)
model = torch.nn.Sequential(torch.nn.Linear(D_in, H), torch.nn.ReLU(), torch.nn.Linear(H, D_out))
loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 0.0001
optimizer = optim.SparseAdam(model.parameters(), lr=learning_rate)