import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.tensor([1, 2, 3], dtype=torch.float)
input2 = torch.tensor([4, 5, 6], dtype=torch.int)
out = torch.promote_types(input1.dtype, input2.dtype)