"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
input_data = torch.tensor([[1.0, (- 1.0)], [1.0, 1.0], [1.0, (- 1.0)]])
target_data = torch.tensor([[1.0], [1.0], [0.0]])
loss_func = torch.nn.HuberLoss(reduction='mean', delta=1.0)
loss = loss_func(input_data, target_data)
print(loss)