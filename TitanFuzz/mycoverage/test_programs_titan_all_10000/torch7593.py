import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 5)
output_data = torch.nn.functional.sigmoid(input_data)