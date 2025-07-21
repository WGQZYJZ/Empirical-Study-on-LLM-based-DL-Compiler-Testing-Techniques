"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
from torch.nn import MSELoss
from torch.nn import HuberLoss
x_data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
y_data = torch.tensor([1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
huber_loss = HuberLoss()
mse_loss = MSELoss()
print('huber_loss: ', huber_loss(x_data, y_data))
print('mse_loss: ', mse_loss(x_data, y_data))