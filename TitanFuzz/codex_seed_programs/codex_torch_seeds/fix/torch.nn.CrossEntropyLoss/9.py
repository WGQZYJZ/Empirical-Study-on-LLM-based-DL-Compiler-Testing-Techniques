"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
input = torch.tensor([[0.1, 0.2, 0.3, 0.4, 0.5], [0.5, 0.4, 0.3, 0.2, 0.1]])
target = torch.tensor([1, 0])
loss = torch.nn.CrossEntropyLoss()
loss_value = loss(input, target)
print(loss_value)
weight = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5])
loss = torch.nn.CrossEntropyLoss(weight=weight)
loss_value = loss(input, target)
print(loss_value)