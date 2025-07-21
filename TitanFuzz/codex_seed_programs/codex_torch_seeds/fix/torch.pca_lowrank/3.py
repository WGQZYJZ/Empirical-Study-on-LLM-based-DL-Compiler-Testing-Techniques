'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pca_lowrank\ntorch.pca_lowrank(A, q=None, center=True, niter=2)\n'
import torch
from torch import Tensor
from torch.autograd import Variable
from typing import Tuple
from torch.nn import Linear
from torch.nn.functional import mse_loss
from torch.optim import SGD
import torch
A = Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)
print(U)
print(S)
print(V)