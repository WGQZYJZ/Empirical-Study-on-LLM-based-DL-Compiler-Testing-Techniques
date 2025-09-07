import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=torch.float)
output = torch.nn.LogSigmoid()