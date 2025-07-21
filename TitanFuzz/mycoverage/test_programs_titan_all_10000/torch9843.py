import torch
from torch import nn
from torch.autograd import Variable
matrices = []
for _ in range(10):
    matrices.append(torch.randn(10, 10))
torch.chain_matmul(*matrices)