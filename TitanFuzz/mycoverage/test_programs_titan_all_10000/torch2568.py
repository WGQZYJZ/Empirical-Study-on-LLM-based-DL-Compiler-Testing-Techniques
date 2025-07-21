import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.rand(3, 4)
input2 = torch.rand(3, 4)
target = torch.rand(3)
loss = torch.nn.functional.cosine_embedding_loss(input1, input2, target)