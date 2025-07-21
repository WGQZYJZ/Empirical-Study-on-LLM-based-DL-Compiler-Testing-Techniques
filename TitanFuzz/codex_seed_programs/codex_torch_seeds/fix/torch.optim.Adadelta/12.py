'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])
W = torch.zeros(1, requires_grad=True)
optimizer = optim.Adadelta([W])
nb_epochs = 10
for epoch in range((nb_epochs + 1)):
    hypothesis = (x_train * W)
    cost = torch.mean(((hypothesis - y_train) ** 2))
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()
    print('Epoch {:4d}/{} W: {:.3f}, Cost: {:.6f}'.format(epoch, nb_epochs, W.item(), cost.item()))