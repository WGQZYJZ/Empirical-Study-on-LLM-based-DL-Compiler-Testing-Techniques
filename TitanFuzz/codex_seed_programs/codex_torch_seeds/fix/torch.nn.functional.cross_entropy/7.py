"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
import torch
(batch_size, n_classes) = (5, 3)
x = torch.randn(batch_size, n_classes)
y = torch.randint(n_classes, size=(batch_size,), dtype=torch.int64)
loss = F.cross_entropy(x, y)
print(loss)
loss = F.cross_entropy(x, y, reduction='sum')
print(loss)