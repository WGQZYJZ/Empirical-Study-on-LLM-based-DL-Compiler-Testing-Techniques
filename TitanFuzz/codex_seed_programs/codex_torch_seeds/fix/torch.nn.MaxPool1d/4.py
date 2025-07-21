'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool1d\ntorch.nn.MaxPool1d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7]]]))
print('input data: ', input)
maxpool = torch.nn.MaxPool1d(kernel_size=3, stride=1, padding=0)
output = maxpool(input)
print('output data: ', output)