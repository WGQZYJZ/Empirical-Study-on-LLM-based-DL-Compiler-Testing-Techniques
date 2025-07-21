"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
target = torch.Tensor([[2, 4, 6], [8, 10, 12]])
loss = torch.nn.SmoothL1Loss()
loss_value = loss(input, target)
print(loss_value)