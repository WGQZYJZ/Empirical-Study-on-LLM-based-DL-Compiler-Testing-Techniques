import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[2, 1], [1, 2]], dtype=torch.float64)
(eigenvalues, eigenvectors) = torch.linalg.eigh(A)