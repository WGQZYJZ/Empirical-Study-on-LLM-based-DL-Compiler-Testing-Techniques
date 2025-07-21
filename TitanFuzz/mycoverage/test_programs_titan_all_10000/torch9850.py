import torch
from torch import nn
from torch.autograd import Variable
input_data = [1, 2, 3, 4, 5]
output_data = torch.QInt32Storage(input_data)