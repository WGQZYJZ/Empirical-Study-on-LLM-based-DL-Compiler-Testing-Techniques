import torch
from torch import nn
from torch.autograd import Variable
A = np.random.randn(5, 5)
A = np.dot(A, A.T)
A = torch.from_numpy(A)
(eigval, eigvec) = torch.linalg.eigh(A)