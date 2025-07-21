import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
target_data = torch.Tensor([[1, 1, 1], [1, 1, 1]])
loss = torch.nn.KLDivLoss(reduction='batchmean')
loss_output = loss(input_data, target_data)