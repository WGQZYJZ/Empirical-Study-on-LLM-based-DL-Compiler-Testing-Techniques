'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svd\ntorch.linalg.svd(A, full_matrices=True, *, out=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
A = torch.randn(3, 2)
print(A)
(U, S, V) = torch.linalg.svd(A)
print(U)
print(S)
print(V)
A = torch.randn(3, 3)
print(A)
(U, S, V) = torch.linalg.svd(A)
print(U)
print(S)
print(V)