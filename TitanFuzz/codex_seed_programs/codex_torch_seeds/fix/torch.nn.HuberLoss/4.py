"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
from torch.nn import HuberLoss
input_data = torch.tensor([1.0, 2.0, 3.0])
target_data = torch.tensor([0.0, 1.0, 2.0])
loss = HuberLoss(reduction='mean', delta=1.0)
loss_value = loss(input_data, target_data)
print('loss:', loss_value.item())