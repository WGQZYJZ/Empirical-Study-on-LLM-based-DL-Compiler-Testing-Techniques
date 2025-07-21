"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch.nn as nn
input_data = torch.Tensor([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]])
target_data = torch.Tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]])
KLDivLoss = nn.KLDivLoss()
loss = KLDivLoss(input_data, target_data)
print(loss)