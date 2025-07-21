"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
import torch
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
target_data = torch.tensor([[2.0, 4.0, 6.0], [8.0, 10.0, 12.0]])
loss = F.mse_loss(input_data, target_data)
print(loss)