import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.long)
embedding = torch.nn.Embedding(10, 3)
output_data = embedding(input_data)