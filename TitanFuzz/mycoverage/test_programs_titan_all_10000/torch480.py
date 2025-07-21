import torch
from torch import nn
from torch.autograd import Variable
logits = torch.randn(2, 3)
gumbel_softmax = torch.nn.functional.gumbel_softmax(logits)