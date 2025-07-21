"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hinge_embedding_loss\ntorch.nn.functional.hinge_embedding_loss(input, target, margin=1.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import numpy as np
import torch
input = Variable(torch.randn(10))
target = Variable(torch.LongTensor(10).random_(2))
print(torch.nn.functional.hinge_embedding_loss(input, target))