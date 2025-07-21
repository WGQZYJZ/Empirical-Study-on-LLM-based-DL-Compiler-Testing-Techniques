"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
from torch.nn import HuberLoss
predictions = torch.tensor([[0.1, 0.1, 0.1], [0.2, 0.2, 0.2], [0.3, 0.3, 0.3]])
targets = torch.tensor([[0.9, 0.9, 0.9], [0.8, 0.8, 0.8], [0.7, 0.7, 0.7]])
loss = HuberLoss(reduction='mean')
print(loss(predictions, targets))
loss = HuberLoss(reduction='sum')
print(loss(predictions, targets))
loss = HuberLoss(reduction='mean', delta=1.0)
print(loss(predictions, targets))