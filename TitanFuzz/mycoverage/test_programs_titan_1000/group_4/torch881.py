import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
output = torch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, out=None)