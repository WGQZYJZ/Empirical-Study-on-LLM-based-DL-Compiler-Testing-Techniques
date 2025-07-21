"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
N = 64
D_in = 1000
H = 100
D_out = 10
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
model = nn.Sequential(nn.Linear(D_in, H), nn.ReLU(), nn.Linear(H, D_out))
loss_fn = nn.BCEWithLogitsLoss(reduction='sum')
learning_rate = 0.0001
for t in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    if ((t % 100) == 99):
        print(t, loss.item())
    model.zero_grad()
    loss.backward()