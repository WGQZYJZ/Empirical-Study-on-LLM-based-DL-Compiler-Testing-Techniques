import torch
from torch import nn
from torch.autograd import Variable
if True:
    cond = torch.tensor([[1, 0], [1, 1]], dtype=torch.bool)
    x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
    y = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
    out = torch.where(cond, x, y)
    print('Output: ', out)