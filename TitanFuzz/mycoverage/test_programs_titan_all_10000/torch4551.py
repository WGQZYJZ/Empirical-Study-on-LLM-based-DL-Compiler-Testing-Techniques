import torch
from torch import nn
from torch.autograd import Variable
input_1 = torch.rand(3, 4)
input_2 = torch.rand(3, 4)
input_3 = torch.rand(3, 4)
output = torch.stack([input_1, input_2, input_3])