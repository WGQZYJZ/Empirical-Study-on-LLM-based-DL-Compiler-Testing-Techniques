import torch
from torch import nn
from torch.autograd import Variable
a = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int)
b = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
torch.promote_types(a.dtype, b.dtype)