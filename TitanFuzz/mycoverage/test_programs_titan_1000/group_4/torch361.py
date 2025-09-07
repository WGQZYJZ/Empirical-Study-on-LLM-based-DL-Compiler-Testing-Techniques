import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
prelu = torch.nn.PReLU()
y = prelu(x)