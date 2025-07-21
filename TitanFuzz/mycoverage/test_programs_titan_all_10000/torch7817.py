import torch
from torch import nn
from torch.autograd import Variable
x = torch.empty_strided(size=[3, 3], stride=[4, 4], dtype=torch.double, layout=torch.strided, device=torch.device('cpu'), requires_grad=True, pin_memory=False)