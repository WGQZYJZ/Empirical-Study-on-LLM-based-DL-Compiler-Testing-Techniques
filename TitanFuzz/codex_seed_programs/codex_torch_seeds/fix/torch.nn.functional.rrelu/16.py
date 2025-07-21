'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)
model = torch.nn.Sequential(torch.nn.Linear(D_in, H), torch.nn.RReLU(), torch.nn.Linear(H, D_out))
loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 0.0001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
for t in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)