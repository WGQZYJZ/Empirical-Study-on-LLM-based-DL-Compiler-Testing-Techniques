import torch
from torch import nn
from torch.autograd import Variable
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
model = torch.nn.Sequential(torch.nn.Linear(D_in, H), torch.nn.ReLU(), torch.nn.Linear(H, D_out))
loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 0.0001
optimizer = torch.optim.SparseAdam(model.parameters(), lr=learning_rate)
for t in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    print(t, loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer