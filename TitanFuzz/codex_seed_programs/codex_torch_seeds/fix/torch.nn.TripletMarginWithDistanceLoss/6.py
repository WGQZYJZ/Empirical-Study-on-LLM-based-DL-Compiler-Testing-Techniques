"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TripletMarginWithDistanceLoss\ntorch.nn.TripletMarginWithDistanceLoss(*, distance_function=None, margin=1.0, swap=False, reduction='mean')\n"
import torch
import torch.nn as nn
import torch
input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
input3 = torch.randn(100, 128)
loss = nn.TripletMarginWithDistanceLoss(margin=1.0, swap=False, reduction='mean')
output = loss(input1, input2, input3)
print(output)