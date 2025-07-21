"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SoftMarginLoss\ntorch.nn.SoftMarginLoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
N = 64
D_in = 1000
H = 100
D_out = 10
x = Variable(torch.randn(N, D_in))
y = Variable(torch.randn(N, D_out), requires_grad=False)
loss_fn = torch.nn.SoftMarginLoss(size_average=False)
w1 = Variable(torch.randn(D_in, H), requires_grad=True)
w2 = Variable(torch.randn(H, D_out), requires_grad=True)
learning_rate = 1e-06
for t in range(500):
    y_pred = x.mm(w1).clamp(min=0).mm(w2)
    loss = loss_fn(y_pred, y)
    print(t, loss.data)