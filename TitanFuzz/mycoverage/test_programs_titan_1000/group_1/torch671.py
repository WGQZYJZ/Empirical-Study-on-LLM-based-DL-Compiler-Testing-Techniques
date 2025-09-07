import torch
from torch import nn
from torch.autograd import Variable
anchor_input = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
positive_input = torch.tensor([[2.0, 3.0, 4.0], [5.0, 6.0, 7.0], [8.0, 9.0, 10.0]])
negative_input = torch.tensor([[3.0, 4.0, 5.0], [6.0, 7.0, 8.0], [9.0, 10.0, 11.0]])
loss = torch.nn.TripletMarginWithDistanceLoss(margin=1.0, swap=False, reduction='mean')
output = loss(anchor_input, positive_input, negative_input)