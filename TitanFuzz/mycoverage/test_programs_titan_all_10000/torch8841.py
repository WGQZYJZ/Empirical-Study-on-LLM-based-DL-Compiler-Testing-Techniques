import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 5.0), (- 3.0), 1.0, 3.0, 5.0])
x = torch.tensor([(- 5.0), (- 3.0), 1.0, 3.0, 5.0])
y = torch.nn.ReLU6()(x)
x = torch.tensor([(- 5.0), (- 3.0), 1.0, 3.0, 5.0])