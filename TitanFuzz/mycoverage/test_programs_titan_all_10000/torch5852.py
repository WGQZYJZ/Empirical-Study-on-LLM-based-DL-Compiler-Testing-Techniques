import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output_data = torch.nn.Softmax(dim=0)(input_data)