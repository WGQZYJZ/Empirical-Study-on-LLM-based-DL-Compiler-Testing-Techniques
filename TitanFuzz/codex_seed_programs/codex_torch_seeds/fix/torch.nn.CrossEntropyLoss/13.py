"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
y_pred = torch.tensor([[0.1, 0.2, 0.7], [0.3, 0.3, 0.4], [0.7, 0.2, 0.1]])
y_true = torch.tensor([2, 1, 0])
loss = torch.nn.CrossEntropyLoss()
print(loss(y_pred, y_true))