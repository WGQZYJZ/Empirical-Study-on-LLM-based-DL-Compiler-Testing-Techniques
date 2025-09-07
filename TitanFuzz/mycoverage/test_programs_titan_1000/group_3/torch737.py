import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.randint(0, 2, (3, 3), dtype=torch.long)
input2 = torch.randint(0, 2, (3, 3), dtype=torch.long)
output = torch.bitwise_xor(input1, input2)