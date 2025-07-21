'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
N = 64
D_in = 1000
H = 100
D_out = 10
x = Variable(torch.randn(N, D_in))
y = Variable(torch.randn(N, D_out), requires_grad=False)
model = nn.Sequential(nn.Linear(D_in, H), nn.AlphaDropout(p=0.5), nn.ReLU(), nn.Linear(H, D_out))
loss_fn = torch.nn.MSELoss(size_average=False)
learning_rate = 0.0001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
for t in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)