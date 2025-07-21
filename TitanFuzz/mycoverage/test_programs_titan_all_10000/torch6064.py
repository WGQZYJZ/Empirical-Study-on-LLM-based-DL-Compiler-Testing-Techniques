import torch
from torch import nn
from torch.autograd import Variable
batch_size = 2
num_classes = 5
logits = torch.randn(batch_size, num_classes)
output = torch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1))