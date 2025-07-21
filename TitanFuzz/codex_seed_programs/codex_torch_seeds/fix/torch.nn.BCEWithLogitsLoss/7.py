"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import torch.nn as nn
input_data = torch.randn(3, requires_grad=True)
target_data = torch.empty(3).random_(2)
loss = nn.BCEWithLogitsLoss()
output = loss(input_data, target_data)
print(output)
output.backward()
print(input_data.grad)