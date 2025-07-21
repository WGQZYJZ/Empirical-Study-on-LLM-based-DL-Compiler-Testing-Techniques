import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9]])
offsets = torch.tensor([0, 4])
torch.nn.EmbeddingBag(10, 3, mode='mean', sparse=False)
torch.nn.EmbeddingBag(10, 3, mode='sum', sparse=False)
torch.nn.EmbeddingBag(10, 3, mode='max', sparse=False)
torch.nn.EmbeddingBag(10, 3, mode='mean', sparse=True)
torch