import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
try:
    torch.package.PackagingError(input_data)
except Exception as e:
    print(e)