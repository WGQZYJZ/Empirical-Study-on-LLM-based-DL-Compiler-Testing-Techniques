'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
max_pool_3d = torch.nn.MaxPool3d(kernel_size=(1, 2, 2), stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
output = max_pool_3d(input)
print('input: ', input)
print('output: ', output)