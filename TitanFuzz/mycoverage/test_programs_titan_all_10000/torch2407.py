import torch
from torch import nn
from torch.autograd import Variable
t1 = torch.empty_strided((2, 3), (1, 2), dtype=torch.float32)