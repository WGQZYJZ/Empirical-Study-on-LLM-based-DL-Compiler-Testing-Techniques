import torch
from torch import nn
from torch.autograd import Variable
if True:
    print('Test sspaddmm')
    input_tensor = torch.rand(1024, 1024)
    mat1 = torch.rand(1024, 1024)
    mat2 = torch.rand(1024, 1024)
    print(torch.Tensor.sspaddmm(input_tensor, mat1, mat2))