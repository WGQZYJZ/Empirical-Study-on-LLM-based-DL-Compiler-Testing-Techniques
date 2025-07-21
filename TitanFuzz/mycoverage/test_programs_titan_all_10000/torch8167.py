import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int)
other_data = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int)
output = torch.bitwise_and(input=input_data, other=other_data)