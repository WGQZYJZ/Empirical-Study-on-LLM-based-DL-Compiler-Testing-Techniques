import torch
from torch import nn
from torch.autograd import Variable
input_data = [1, 2, 3, 4, 5]
QInt8_data = torch.QUInt8Storage(input_data)