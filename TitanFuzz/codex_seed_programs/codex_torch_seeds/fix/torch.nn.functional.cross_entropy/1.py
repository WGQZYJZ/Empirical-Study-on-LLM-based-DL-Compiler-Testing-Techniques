"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
batch_n = 100
n_class = 5
dim = 50
x = torch.randn(batch_n, dim)
y = torch.empty(batch_n, dtype=torch.long).random_(n_class)
loss = nn.CrossEntropyLoss()
output = loss(x, y)
print(output)