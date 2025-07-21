import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
input2 = torch.tensor([[3, 4, 5], [6, 7, 8]], dtype=torch.float)
target = torch.tensor([(- 1), 1], dtype=torch.float)
torch.nn.functional.cosine_embedding_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')