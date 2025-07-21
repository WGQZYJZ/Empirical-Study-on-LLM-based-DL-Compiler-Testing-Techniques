import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 5.0), (- 4.0), (- 3.0), (- 2.0), (- 1.0), 1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.nn.Sigmoid()(x)