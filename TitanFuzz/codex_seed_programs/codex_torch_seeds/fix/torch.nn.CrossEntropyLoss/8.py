"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input_data = torch.tensor([[0.1, 0.2, 0.3], [0.3, 0.2, 0.1]])
target_data = torch.tensor([1, 0])
cross_entropy_loss = nn.CrossEntropyLoss()
loss = cross_entropy_loss(input_data, target_data)
print('The loss is: ', loss)