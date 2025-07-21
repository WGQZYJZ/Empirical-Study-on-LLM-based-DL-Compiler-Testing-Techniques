"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch
data = torch.randn(5, 3)
label = torch.tensor([1, 0, 2, 1, 1])
loss = torch.nn.CrossEntropyLoss()
output = loss(data, label)
print(output)