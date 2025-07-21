import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
input2 = torch.tensor([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype=torch.float32)
cosine_similarity = torch.nn.CosineSimilarity(dim=0, eps=1e-08)