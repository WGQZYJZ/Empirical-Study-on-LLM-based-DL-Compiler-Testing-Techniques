import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 4)
y = torch.rand(3, 4)
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cosine_similarity(x, y)