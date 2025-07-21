'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
tensor = torch.randn(2, 3)
print(tensor)
print(tensor.shape)
tensor = torch.reshape(tensor, (3, 2))
print(tensor)
print(tensor.shape)