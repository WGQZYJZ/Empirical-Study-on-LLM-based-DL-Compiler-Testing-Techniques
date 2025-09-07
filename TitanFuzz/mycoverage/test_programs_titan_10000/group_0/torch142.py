import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(1, 1, 5, 5)
output = torch.nn.functional.local_response_norm(input, size=2)