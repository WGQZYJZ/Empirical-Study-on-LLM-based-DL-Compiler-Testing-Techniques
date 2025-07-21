"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
y_pred = Variable(torch.randn(3, 4))
y_true = Variable(torch.randn(3, 4))
loss = torch.nn.BCEWithLogitsLoss()
output = loss(y_pred, y_true)
print(output)