import torch
from torch import nn
from torch.autograd import Variable
anchor = torch.tensor([[1.0, 1.0]], dtype=torch.float)
positive = torch.tensor([[2.0, 2.0]], dtype=torch.float)
negative = torch.tensor([[3.0, 3.0]], dtype=torch.float)
distance_function = torch.nn.PairwiseDistance(p=2)
margin = 1.0
swap = False
reduction = 'mean'
loss = torch.nn.TripletMarginWithDistanceLoss(distance_function=distance_function, margin=margin, swap=swap, reduction=reduction)