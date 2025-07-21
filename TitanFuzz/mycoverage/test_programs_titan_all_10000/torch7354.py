import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
output_data = torch.dequantize(input_data)