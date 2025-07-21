"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
x = torch.randn(64, 10)
y = torch.randint(low=0, high=10, size=(64,))
loss = F.cross_entropy(x, y)
print(loss)
"\nTask 4: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
loss = F.cross_entropy(x, y, reduction='sum')
print(loss)