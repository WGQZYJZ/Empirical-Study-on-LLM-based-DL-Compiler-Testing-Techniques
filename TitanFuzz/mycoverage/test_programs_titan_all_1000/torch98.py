import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(0, 10, (5, 5))
output = torch.tril(input_data, diagonal=0)