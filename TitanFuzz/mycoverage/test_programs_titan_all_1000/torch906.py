import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9]]], dtype=torch.float32)
kernel_size = 3
stride = 1
padding = 0
y = torch.nn.functional.max_pool1d(x, kernel_size, stride, padding)