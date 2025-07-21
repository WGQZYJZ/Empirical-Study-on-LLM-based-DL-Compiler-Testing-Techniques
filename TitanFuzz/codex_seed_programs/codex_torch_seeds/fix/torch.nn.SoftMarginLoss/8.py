"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SoftMarginLoss\ntorch.nn.SoftMarginLoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import numpy as np
import torch
input_tensor = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
print(input_tensor)
target_tensor = torch.tensor([[0.0], [1.0], [1.0], [0.0]])
print(target_tensor)
loss_fn = torch.nn.SoftMarginLoss()
loss = loss_fn(input_tensor, target_tensor)
print(loss)