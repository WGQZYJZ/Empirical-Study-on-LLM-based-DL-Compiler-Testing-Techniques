"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
y_pred = torch.tensor([[1.0, 0.0], [0.0, 1.0]], requires_grad=True)
y_true = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
loss = nn.BCEWithLogitsLoss()
loss_value = loss(y_pred, y_true)
print(loss_value)
pos_weight = torch.tensor([0.1, 0.9])
loss = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
loss_value = loss(y_pred, y_true)
print(loss_value)