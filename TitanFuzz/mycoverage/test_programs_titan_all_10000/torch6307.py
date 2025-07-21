import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50).float()
torch.nn.functional.max_pool1d(input, kernel_size=2, stride=2)