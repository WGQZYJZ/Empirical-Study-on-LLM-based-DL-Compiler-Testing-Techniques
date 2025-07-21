import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 2, 3, 4, 5])
output = torch.is_complex(input)