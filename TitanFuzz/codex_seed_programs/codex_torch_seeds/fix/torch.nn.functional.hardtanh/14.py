'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = Variable(torch.randn(5, 3))
print(x)
print(F.hardtanh(x))