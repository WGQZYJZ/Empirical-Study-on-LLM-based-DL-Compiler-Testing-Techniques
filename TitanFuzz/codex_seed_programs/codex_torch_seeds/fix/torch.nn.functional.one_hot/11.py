'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
import torch.nn.functional as F
x = torch.tensor([1, 2, 3])
print('x:', x)
y = F.one_hot(x, num_classes=10)
print('y:', y)