"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
import torch.nn as nn
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
target_data = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
huber_loss = nn.HuberLoss(reduction='mean', delta=1.0)
loss = huber_loss(input_data, target_data)
print(loss)