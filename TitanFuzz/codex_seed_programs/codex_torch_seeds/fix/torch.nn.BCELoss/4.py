"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCELoss\ntorch.nn.BCELoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
y_pred = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4]])
y_true = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4]])
loss_func = torch.nn.BCELoss()
loss = loss_func(y_pred, y_true)
print(loss)