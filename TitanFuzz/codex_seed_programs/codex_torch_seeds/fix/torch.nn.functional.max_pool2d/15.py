'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = Variable(torch.Tensor([[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]]]))
print(x)
print(x.size())
print(F.max_pool2d(x, (2, 2)))