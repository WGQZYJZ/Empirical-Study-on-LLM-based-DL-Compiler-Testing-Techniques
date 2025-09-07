import torch
from torch import nn
from torch.autograd import Variable
t1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
t2 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
t3 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
torch.addcmul(t1, t2, t3)