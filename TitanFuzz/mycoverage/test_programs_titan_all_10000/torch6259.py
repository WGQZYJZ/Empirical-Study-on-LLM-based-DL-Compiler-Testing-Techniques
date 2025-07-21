import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 20)
torch.compiled_with_cxx11_abi()