import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0.0, 0.5, 1.0])
output = torch.arccos(input_data)