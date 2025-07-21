import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, requires_grad=True)
with torch.no_grad():
    output = (input_data * 2)