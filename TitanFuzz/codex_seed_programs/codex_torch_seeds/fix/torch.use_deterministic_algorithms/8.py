'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
from torch.autograd import Variable
import numpy as np
x = Variable(torch.randn(1, 1, 3, 3))
y = Variable(torch.randn(1, 1, 3, 3))
torch.use_deterministic_algorithms(mode=True)
print(torch.add(x, y))
print(torch.add(x, y))
torch.use_deterministic_algorithms(mode=False)
print(torch.add(x, y))
print(torch.add(x, y))