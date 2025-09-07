import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 3, 3, 3))
input[0, 0, :, :, :] = torch.Tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
pool = torch.nn.MaxPool3d(kernel_size=2, stride=2, padding=0)
output = pool(input)