"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCELoss\ntorch.nn.BCELoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
from torch.autograd import Variable
y_true = Variable(torch.Tensor([1, 0, 0, 1]))
y_pred = Variable(torch.Tensor([0.9, 0.1, 0.2, 0.8]))
bce_loss = nn.BCELoss()
loss = bce_loss(y_pred, y_true)
print(loss)