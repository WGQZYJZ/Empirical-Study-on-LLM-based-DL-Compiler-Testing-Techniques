import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(100000)
y = torch.rand(100000)
torch.compiled_with_cxx11_abi()