import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=torch.float32)
output = torch.nanmedian(input, dim=(- 1), keepdim=False, out=None)
output = torch.nanmedian(input, dim=(- 1), keepdim=True, out=None)
output = torch.nanmedian(input, dim=1, keepdim=False, out=None)
output = torch.nanmedian(input, dim=1, keepdim=True, out=None)