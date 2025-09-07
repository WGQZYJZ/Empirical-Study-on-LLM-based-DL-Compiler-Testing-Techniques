import torch
from torch import nn
from torch.autograd import Variable
anchor = torch.tensor([[1, 2, 3]])
positive = torch.tensor([[2, 3, 4]])
negative = torch.tensor([[3, 4, 5]])
loss = torch.nn.TripletMarginWithDistanceLoss()
loss(anchor, positive, negative)
anchor = torch.tensor([[1, 2, 3]])
positive = torch.tensor([[2, 3, 4]])
negative = torch.tensor([[3, 4, 5]])
loss = torch.nn.TripletMarginWithDistanceLoss(margin=1.0, swap=True)
loss(anchor, positive, negative)
anchor = torch.tensor([[1, 2, 3]])
positive = torch.tensor([[2, 3, 4]])
negative = torch.tensor([[3, 4, 5]])