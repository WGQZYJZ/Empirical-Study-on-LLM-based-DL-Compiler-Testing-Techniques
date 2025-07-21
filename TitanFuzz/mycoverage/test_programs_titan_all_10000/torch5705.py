import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 3)
threshold = 0.5
value = 0.2
output = torch.nn.functional.threshold(input, threshold, value)