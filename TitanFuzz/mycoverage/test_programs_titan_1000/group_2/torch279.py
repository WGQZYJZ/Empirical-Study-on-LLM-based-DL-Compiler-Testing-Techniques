import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
stick_breaking_transform = torch.distributions.transforms.StickBreakingTransform(cache_size=0)