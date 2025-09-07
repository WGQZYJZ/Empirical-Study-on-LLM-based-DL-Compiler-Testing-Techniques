import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, requires_grad=True)
target = torch.randint(low=0, high=1, size=(10,), dtype=torch.long)
loss = torch.nn.functional.hinge_embedding_loss(input, target)