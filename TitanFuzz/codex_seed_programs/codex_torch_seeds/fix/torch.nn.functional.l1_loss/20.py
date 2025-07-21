"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.l1_loss\ntorch.nn.functional.l1_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
input = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
target = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
l1_loss = torch.nn.functional.l1_loss(input, target)
print(l1_loss)
l1_loss = torch.nn.functional.l1_loss(input, target, size_average=False)
print(l1_loss)
l1_loss = torch.nn.functional.l1_loss(input, target, reduce=True)
print(l1_loss)
l1_loss = torch.nn.functional.l1_loss(input, target, reduction='sum')
print(l1_loss)