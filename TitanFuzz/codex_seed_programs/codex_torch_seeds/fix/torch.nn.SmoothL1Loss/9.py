"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
import torch
x = torch.tensor([(- 1.0), 1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.tensor([(- 1.0), 1.0, 2.0, 3.0, 4.0, 5.0])
smoothL1Loss = torch.nn.SmoothL1Loss()
loss = smoothL1Loss(x, y)
print(loss)