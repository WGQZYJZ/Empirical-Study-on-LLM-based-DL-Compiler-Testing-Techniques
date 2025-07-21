"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
import torch
input_data = torch.tensor([[0.0, 0.0], [1.0, 1.0], [1.0, 0.0], [0.0, 1.0]])
target_data = torch.tensor([[0.0], [1.0], [1.0], [0.0]])
loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
loss_value = loss(input_data, target_data)
print(loss_value)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(reduction='mean', beta=1.0)\n"
import torch