'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adagrad\ntorch.optim.Adagrad(params, lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0, eps=1e-10)\n'
import torch
import torch.nn as nn
import torch.optim as optim
X = torch.randn(10, 3)
Y = torch.randn(10, 2)
model = nn.Sequential(nn.Linear(3, 10), nn.ReLU(), nn.Linear(10, 2))
optimizer = optim.Adagrad(model.parameters(), lr=0.1)
for epoch in range(50):
    Y_pred = model(X)
    loss = torch.nn.functional.mse_loss(Y_pred, Y)
    print('epoch: ', epoch, ' loss: ', loss.item())
    optimizer.zero_grad()