import torch
from torch import nn
from torch.autograd import Variable
torch.__version__
A = torch.rand(3, 3)
A
torch.linalg.eigh(A)
torch.linalg.eigh(A, UPLO='U')
torch.linalg.eigh(A, UPLO='L')
torch.linalg.eigh(A, UPLO='L', out=(torch.rand(3), torch.rand(3, 3)))
torch.linalg.eigh(A, UPLO='L', out=(torch.rand(3), torch.rand(3, 3)))[0]
torch.linalg.eigh(A, UPLO='L', out=(torch.rand(3), torch.rand(3, 3)))[1]