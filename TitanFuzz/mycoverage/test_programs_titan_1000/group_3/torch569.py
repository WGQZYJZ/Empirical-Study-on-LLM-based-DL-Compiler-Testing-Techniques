import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1, 2], [3, 4]]).float()
B = torch.tensor([[1, 2], [3, 4]]).float()
torch.linalg.lstsq(A, B, rcond=None, driver=None)