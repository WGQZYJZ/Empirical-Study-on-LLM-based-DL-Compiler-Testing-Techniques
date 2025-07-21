import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
model = torch.nn.Identity()
output_data = model(input_data)