import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 2), (- 1), 0, 1, 2])
y = torch.nn.Softsign()(x)