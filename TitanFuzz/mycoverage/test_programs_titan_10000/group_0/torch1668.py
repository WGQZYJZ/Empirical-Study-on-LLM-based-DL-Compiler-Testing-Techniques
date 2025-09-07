import torch
from torch import nn
from torch.autograd import Variable

if True:
    input = torch.randn(3, 3)
    print('Input data: ', input)
    output = torch.matrix_rank(input)
    print('Output: ', output)