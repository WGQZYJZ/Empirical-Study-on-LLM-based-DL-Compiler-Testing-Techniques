import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[0.2, 0.4, 0.4]])
output = torch.multinomial(input_data, 2)