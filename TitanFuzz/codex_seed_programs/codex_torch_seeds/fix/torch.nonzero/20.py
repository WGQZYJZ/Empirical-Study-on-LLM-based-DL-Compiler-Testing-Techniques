'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
from torch.autograd import Variable
a = torch.randn(3, 3)
print(a)
import torch
a = torch.randn(3, 3)
print(a)
print(torch.nonzero(a))
print(torch.nonzero(a, as_tuple=True))
out = torch.LongTensor()
torch.nonzero(a, out=out)
print(out)