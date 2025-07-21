import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype=torch.float32)
x = x.view(1, 4, 4)
max_pool1d = torch.nn.MaxPool1d(kernel_size=2, stride=2)
y = max_pool1d(x)