import torch
from torch import nn
from torch.autograd import Variable
if True:
    input_tensor = torch.randn(2, 3)
    print(input_tensor)
    torch.nn.init.sparse_(input_tensor, sparsity=0.5, std=0.01)
    print(input_tensor)