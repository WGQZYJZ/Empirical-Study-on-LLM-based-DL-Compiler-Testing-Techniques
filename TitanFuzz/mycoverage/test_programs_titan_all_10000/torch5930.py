import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
target_data = torch.randn(10)
torch.compiled_with_cxx11_abi()