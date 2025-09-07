import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
out = torch.topk(x, 2)
out = torch.topk(x, k=2, dim=0)
out = torch.topk(x, k=2, dim=1)
out = torch.topk(x, k=2, dim=1, largest=False)