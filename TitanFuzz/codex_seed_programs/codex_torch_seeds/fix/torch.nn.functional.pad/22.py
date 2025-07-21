"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x)
y = torch.nn.functional.pad(x, (1, 2), mode='constant', value=0)
print(y)