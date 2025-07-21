import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.randn(2, 3)
tensor2 = torch.Tensor.sort(tensor, dim=(- 1), descending=False)
tensor3 = torch.Tensor.sort(tensor, dim=(- 1), descending=True)