import torch
from torch import nn
from torch.autograd import Variable
if True:
    A = torch.randn(3, 4)
    print('Input matrix A: \n', A)
    (U, S, V) = torch.svd(A)
    print('U: \n', U)
    print('S: \n', S)
    print('V: \n', V)
    print('U * S * V.T: \n', U.mm(torch.diag(S)).mm(V.t()))