import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
x = x.reshape(1, 1, 5, 5)
pooling = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=0)
y = pooling(x)