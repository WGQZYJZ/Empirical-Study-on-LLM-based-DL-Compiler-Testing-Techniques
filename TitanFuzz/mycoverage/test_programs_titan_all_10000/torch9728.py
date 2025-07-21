import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
threshold = 0
value = 0
output = torch.nn.functional.threshold(input, threshold, value)