import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]], dtype=torch.float32)
output = torch.nn.functional.lp_pool2d(input, norm_type=2, kernel_size=2, stride=2)