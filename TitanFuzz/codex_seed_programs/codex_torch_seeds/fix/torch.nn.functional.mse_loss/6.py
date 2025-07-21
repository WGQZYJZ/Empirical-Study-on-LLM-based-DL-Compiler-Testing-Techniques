"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
input = torch.Tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
target = torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
loss = torch.nn.functional.mse_loss(input, target)
print('loss:', loss)