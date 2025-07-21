import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 3, 3, 3))
input[0, 0, :, :, :] = torch.Tensor([[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3], [3, 3, 3]]])
output = torch.nn.functional.max_pool3d(input, kernel_size=2, stride=2)