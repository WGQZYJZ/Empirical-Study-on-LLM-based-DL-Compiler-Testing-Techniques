import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, D, H, W) = (2, 3, 4, 5, 6)
x = Variable(torch.randn(N, C, D, H, W).type(dtype), requires_grad=True)
pooled_x = torch.nn.functional.max_pool3d(x, kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=0)