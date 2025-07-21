import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]])
stick_breaking = torch.distributions.transforms.StickBreakingTransform(cache_size=0)
y = stick_breaking(x)