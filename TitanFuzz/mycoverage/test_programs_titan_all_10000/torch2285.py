import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
padding = (1, 1, 2, 2)
zero_pad = torch.nn.ZeroPad2d(padding)
result = zero_pad(data)