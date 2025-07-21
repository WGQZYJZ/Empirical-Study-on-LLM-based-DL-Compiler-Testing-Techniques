"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch
x = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
y = torch.tensor([1, 0])
loss = torch.nn.CrossEntropyLoss()
output = loss(x, y)
print(output)