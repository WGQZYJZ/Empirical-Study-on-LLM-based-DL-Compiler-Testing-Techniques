import torch
from torch import nn
from torch.autograd import Variable

if True:
    input_tensor = torch.randn(1, 3)
    other = torch.randn(1, 3)
    print(torch.Tensor.maximum(input_tensor, other))