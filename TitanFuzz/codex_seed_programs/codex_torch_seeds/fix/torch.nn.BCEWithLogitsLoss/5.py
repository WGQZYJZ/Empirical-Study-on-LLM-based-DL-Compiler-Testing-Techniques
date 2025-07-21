"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
y = torch.randn(2, 2)
target = torch.empty(2, 2).random_(2)
loss = nn.BCEWithLogitsLoss()
output = loss(y, target)
print(output)