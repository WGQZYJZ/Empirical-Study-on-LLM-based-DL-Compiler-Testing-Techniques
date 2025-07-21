'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
import numpy as np
x = torch.tensor([[0, 1, 2], [3, 4, 5]])
print(x)
print(torch.nn.functional.one_hot(x, num_classes=6))