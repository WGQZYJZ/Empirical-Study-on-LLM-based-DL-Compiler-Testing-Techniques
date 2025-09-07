import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
topk_data = torch.topk(data, 2, dim=1)
for i in range(len(topk_data[0])):
    print(topk_data[0][i])
for i in range(len(topk_data[1])):
    print