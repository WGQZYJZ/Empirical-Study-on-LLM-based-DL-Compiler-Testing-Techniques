'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)
w1 = Variable(torch.randn(D_in, H).type(dtype), requires_grad=True)
w2 = Variable(torch.randn(H, D_out).type(dtype), requires_grad=True)
learning_rate = 1e-06
optimizer = torch.optim.SparseAdam([w1, w2], lr=learning_rate)
for t in range(500):
    y_pred = x.mm(w1).clamp(min=0).mm(w2)