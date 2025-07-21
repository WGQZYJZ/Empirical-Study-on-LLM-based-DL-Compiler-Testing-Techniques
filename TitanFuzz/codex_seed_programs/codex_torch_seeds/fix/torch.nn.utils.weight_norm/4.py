"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
from torch.nn.utils import weight_norm
import torch
x = torch.randn(2, 3)
w = weight_norm(torch.nn.Linear(3, 2))
print(w(x))