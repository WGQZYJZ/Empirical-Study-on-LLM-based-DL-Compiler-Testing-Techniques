'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trace\ntorch.trace(input)\n'
import torch
print(torch.__version__)
x = torch.arange(12).reshape(3, 4)
print(x)
print(torch.trace(x))