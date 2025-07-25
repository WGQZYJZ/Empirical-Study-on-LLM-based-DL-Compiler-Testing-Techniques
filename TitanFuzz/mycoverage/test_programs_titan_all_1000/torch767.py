import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[[[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0], [8.0, 9.0, 10.0, 11.0], [12.0, 13.0, 14.0, 15.0]]]]])
indices = torch.tensor([[[[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]]]])
output = torch.nn.functional.max_unpool3d(input, indices, kernel_size=(2, 2, 2))