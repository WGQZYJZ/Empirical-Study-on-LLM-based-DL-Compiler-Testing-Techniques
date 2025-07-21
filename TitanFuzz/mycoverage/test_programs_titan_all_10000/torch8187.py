import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
result = torch.median(data, dim=(- 1))