import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
result = torch.nn.functional.normalize(data, p=2.0, dim=1, eps=1e-12, out=None)
data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
result = torch.nn.functional.normalize(data, p=1.0, dim=1, eps=1e-12, out=None)