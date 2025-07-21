import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])
pad_value = torch.tensor(0)
pad_size = (1, 2, 1, 2)
pad_layer = torch.nn.ConstantPad3d(pad_size, pad_value)
output_data = pad_layer(input_data)