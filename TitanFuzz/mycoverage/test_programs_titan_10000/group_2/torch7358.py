import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor(np.random.randn(10, 10), dtype=torch.float32)
other = torch.tensor(np.random.randn(10, 10), dtype=torch.float32)
y = torch.igammac(x, other)