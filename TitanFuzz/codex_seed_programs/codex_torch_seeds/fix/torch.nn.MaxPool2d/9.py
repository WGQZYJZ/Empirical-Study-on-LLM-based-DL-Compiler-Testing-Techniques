'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]]]))
max_pooling = torch.nn.MaxPool2d(kernel_size=2, stride=1, padding=0)
output = max_pooling(input)
print(output)