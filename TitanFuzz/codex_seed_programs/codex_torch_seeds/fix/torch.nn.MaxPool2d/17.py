'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.Tensor(1, 1, 4, 4))
input[0, 0, :, :] = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
maxpool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
output = maxpool(input)
print(output)