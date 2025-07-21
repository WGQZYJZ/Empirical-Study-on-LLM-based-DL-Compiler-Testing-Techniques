"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCELoss\ntorch.nn.BCELoss(weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
prediction = torch.rand(10, 1)
target = torch.rand(10, 1)
loss_func = torch.nn.BCELoss()
loss = loss_func(prediction, target)
print(loss)