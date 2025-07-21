'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.sigmoid\ntorch.nn.functional.sigmoid(input)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.nn.functional.sigmoid(x)
print(y)