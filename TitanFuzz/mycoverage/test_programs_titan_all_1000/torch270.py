import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4, 4, 4)
torch.nn.MaxUnpool3d(kernel_size=2, stride=2, padding=0)