"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
from torch.nn import HuberLoss
input = torch.tensor([(- 1.0), 0.0, 1.0, 2.0, 3.0, 4.0], requires_grad=True)
target = torch.tensor([(- 1.0), 0.0, 1.0, 2.0, 3.0, 4.0])
huber_loss = HuberLoss()
loss = huber_loss(input, target)
print(loss)
loss.backward()
print(input.grad)