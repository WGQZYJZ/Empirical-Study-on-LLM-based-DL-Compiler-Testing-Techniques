import torch
from torch import nn
from torch.autograd import Variable
y_pred = Variable(torch.randn(3, 4))
y_true = Variable(torch.randn(3, 4))
loss = torch.nn.BCEWithLogitsLoss()
output = loss(y_pred, y_true)