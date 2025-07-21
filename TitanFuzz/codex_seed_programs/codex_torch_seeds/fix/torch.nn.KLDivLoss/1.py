"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch.nn as nn
input_data = torch.tensor([[(- 0.2), 0.3, 0.1], [0.2, 0.2, 0.2]])
target_data = torch.tensor([[0.1, 0.2, 0.7], [0.2, 0.2, 0.6]])
loss = nn.KLDivLoss()
loss_value = loss(input_data, target_data)
print(loss_value)