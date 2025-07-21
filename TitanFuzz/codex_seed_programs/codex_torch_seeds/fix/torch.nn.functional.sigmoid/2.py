'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.sigmoid\ntorch.nn.functional.sigmoid(input)\n'
import torch
import torch.nn.functional as F
x = torch.tensor([1.0, 2.0, 3.0])
print(F.sigmoid(x))
print(F.softmax(x, dim=0))
print(F.softmax(x, dim=0).sum())
print(F.log_softmax(x, dim=0))