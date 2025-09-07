import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(100, 100)
torch.compiled_with_cxx11_abi()