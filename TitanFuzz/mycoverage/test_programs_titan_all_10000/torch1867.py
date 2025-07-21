import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0])
output = torch.acosh(input_data)