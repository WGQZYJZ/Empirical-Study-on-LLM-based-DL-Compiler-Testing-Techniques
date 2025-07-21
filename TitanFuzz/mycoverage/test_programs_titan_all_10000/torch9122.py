import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 7, 7)
torch.nn.functional.unfold(input, kernel_size=3, dilation=1, padding=0, stride=1)
torch.nn.functional.unfold(input, kernel_size=3, dilation=2, padding=0, stride=1)
torch.nn.functional.unfold(input, kernel_size=3, dilation=1, padding=1, stride=1)
torch.nn.functional.unfold(input, kernel_size=3, dilation=1, padding=0, stride=2)
torch.nn.functional.unfold(input, kernel_size=3, dilation=1, padding=0, stride=1).shape