import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.randn(3, 5)
input2 = torch.randn(3, 5)
target = torch.tensor([(- 1), 1, 1], dtype=torch.float)
loss = torch.nn.functional.cosine_embedding_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')