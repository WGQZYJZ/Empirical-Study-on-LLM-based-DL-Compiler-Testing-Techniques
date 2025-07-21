import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 1.0, 2.0])
softshrink = torch.nn.Softshrink(lambd=0.5)
output = softshrink(input_data)