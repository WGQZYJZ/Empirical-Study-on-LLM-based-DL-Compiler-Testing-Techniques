import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0.0, 30.0, 45.0, 60.0, 90.0], dtype=torch.float)
output = torch.cos(input_data)