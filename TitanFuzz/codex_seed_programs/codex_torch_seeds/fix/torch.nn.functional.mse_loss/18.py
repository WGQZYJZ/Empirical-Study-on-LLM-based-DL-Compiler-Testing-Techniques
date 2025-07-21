"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch
input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float)
target_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float)
loss = torch.nn.functional.mse_loss(input_data, target_data)
print(loss)
print(loss.shape)
print(loss.dtype)