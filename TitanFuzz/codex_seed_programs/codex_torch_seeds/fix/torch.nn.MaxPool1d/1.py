'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool1d\ntorch.nn.MaxPool1d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
input_data = Variable(torch.Tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]))
max_pooling_layer = nn.MaxPool1d(2, stride=1, padding=0)
output = max_pooling_layer(input_data)
print('input_data: ', input_data)
print('output: ', output)