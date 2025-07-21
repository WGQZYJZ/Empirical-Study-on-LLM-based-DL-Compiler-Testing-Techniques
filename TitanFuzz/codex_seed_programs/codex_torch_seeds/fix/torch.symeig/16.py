'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
import numpy as np
a = torch.randn(3, 3)
a = (a + a.t())
print(a)
(e, v) = torch.symeig(a, eigenvectors=True)
print(e)
print(v)
print(torch.mm(torch.mm(v, torch.diag(e)), v.t()))