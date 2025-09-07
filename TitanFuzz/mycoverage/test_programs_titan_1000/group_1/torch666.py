import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.linspace((- 10), 10, 10, requires_grad=True)
output_data = torch.sigmoid(input_data)