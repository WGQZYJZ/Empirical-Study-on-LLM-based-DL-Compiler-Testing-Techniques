'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch
input_data = Variable(torch.Tensor([[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]]]))
pooling = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)
pooling(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F