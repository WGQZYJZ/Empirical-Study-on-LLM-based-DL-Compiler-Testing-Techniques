import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
(w, v) = torch.eig(A, eigenvectors=True)