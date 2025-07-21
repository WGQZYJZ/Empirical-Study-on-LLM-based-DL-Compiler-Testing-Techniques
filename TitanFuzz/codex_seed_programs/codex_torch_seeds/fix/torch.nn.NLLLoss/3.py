"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.NLLLoss\ntorch.nn.NLLLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import numpy as np
import torch
x = torch.randn(3, requires_grad=True)
y = torch.tensor([1, 0, 3], dtype=torch.int64)
loss = torch.nn.NLLLoss()
output = loss(torch.log_softmax(x, dim=0), y)
output.backward()
print(x.grad)
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import numpy as np
import torch
x = torch.rand