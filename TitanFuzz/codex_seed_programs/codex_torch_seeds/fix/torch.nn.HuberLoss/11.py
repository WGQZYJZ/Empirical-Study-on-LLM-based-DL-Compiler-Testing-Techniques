"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
from torch.nn import HuberLoss
delta = 1.0
input_data = torch.Tensor([[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]])
target_data = torch.Tensor([[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]])
loss_fn = HuberLoss(reduction='mean', delta=delta)
loss = loss_fn(input_data, target_data)
print('Loss: ', loss)