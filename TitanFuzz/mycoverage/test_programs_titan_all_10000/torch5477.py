import torch
from torch import nn
from torch.autograd import Variable
input_data = [1, 0, 0, 1, 1, 0, 1, 1]
output = torch.BoolStorage(input_data)