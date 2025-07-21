import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange((- 5.0), 5.0, 0.1)
x = x.view(1, (- 1))
y = torch.arange((- 5.0), 5.0, 0.1)
y = y.view((- 1), 1)
z = torch.sigmoid(torch.add(x, y))
result = torch.nn.functional.threshold(z, 0.5, 0.0)