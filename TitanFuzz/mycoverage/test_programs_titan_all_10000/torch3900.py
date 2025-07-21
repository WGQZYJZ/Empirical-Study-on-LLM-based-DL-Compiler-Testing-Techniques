import torch
from torch import nn
from torch.autograd import Variable
if True:
    print('Task 1: import PyTorch')
    print(('-' * 15))
    print('PyTorch version: ', torch.__version__)
    print(('-' * 15))
    print('Task 2: Generate input data')
    A = torch.randn(2, 2)
    print('Input data: \n', A)
    print('Task 3: Call the API torch.linalg.inv_ex')
    print(('-' * 15))
    print('Result: ', torch.linalg.inv_ex(A))
    print(('-' * 15))
    print('Task 3: Call the API torch.linalg.inv_ex')
    print(('-' * 15))
    print('Result: ', torch.linalg.inv_ex(A, check_errors=True))
    print(('-' * 15))