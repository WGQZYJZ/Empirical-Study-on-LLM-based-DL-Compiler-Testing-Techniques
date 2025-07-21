import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[1, 2, 3], [4, 5, 6]]])
output = torch.nn.functional.pad(input, pad=(0, 1, 0, 1), mode='constant', value=0)