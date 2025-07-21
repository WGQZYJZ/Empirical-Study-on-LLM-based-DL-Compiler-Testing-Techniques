'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3], [4, 5, 6]]]]))
print('Input data: ', input)
max_pool_2d = torch.nn.MaxPool2d(kernel_size=2, stride=1)
output = max_pool_2d(input)
print('Output data: ', output)