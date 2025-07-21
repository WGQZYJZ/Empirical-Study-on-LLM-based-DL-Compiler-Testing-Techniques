import torch
from torch import nn
from torch.autograd import Variable
if True:
    import torch
    A = torch.rand(3, 3)
    print('A: \n{}'.format(A))
    A_pinv = torch.linalg.pinv(A)
    print('A_pinv: \n{}'.format(A_pinv))