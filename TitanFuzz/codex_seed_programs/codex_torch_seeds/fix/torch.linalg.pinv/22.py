'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
a = torch.randn(3, 3)
print(torch.linalg.pinv(a))