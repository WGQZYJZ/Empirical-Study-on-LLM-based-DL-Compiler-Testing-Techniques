'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
input = input.view(1, 1, 4, 4)
print(input)
max_pool_layer = torch.nn.MaxPool2d(2, stride=2)
output = max_pool_layer(input)
print(output)
'\nMax Pooling with a 2x2 kernel and stride of 2\nMax Pooling with a 2x2 kernel and stride of 1\nMax Pooling with a 2x2 kernel and stride of 1\n'