import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]], dtype=torch.float32)
indices = torch.tensor([[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]], dtype=torch.long)
kernel_size = 2
output = torch.nn.functional.max_unpool1d(input, indices, kernel_size)