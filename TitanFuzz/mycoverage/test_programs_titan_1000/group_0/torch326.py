import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 4, 5)
output = torch.resolve_conj(input_data)