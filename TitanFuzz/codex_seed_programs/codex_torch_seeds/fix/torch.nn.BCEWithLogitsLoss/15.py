"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import torch.nn as nn
import numpy as np
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
bce_with_logits_loss = nn.BCEWithLogitsLoss()
output = bce_with_logits_loss(input, target)
print(output)
output.backward()
print(input.grad)